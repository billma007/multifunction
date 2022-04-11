import win32api, win32con, win32gui_struct, win32gui
import os, tkinter as tk

class SysTrayIcon (object):
    '''SysTrayIcon类用于显示任务栏图标'''
    QUIT = 'QUIT'
    SPECIAL_ACTIONS = [QUIT]
    FIRST_ID = 5320
    def __init__(self, icon, hover_text, menu_options, on_quit, tk_window = None, default_menu_index=None, window_class_name = None):
        '''
        icon         需要显示的图标文件路径
        hover_text   鼠标停留在图标上方时显示的文字
        menu_options 右键菜单，格式: (('a', None, callback), ('b', None, (('b1', None, callback),)))
        on_quit      传递退出函数，在执行退出时一并运行
        tk_window    传递Tk窗口，s.root，用于单击图标显示窗口
        default_menu_index 不显示的右键菜单序号
        window_class_name  窗口类名
        '''
        self.icon = icon
        self.hover_text = hover_text
        self.on_quit = on_quit
        self.root = tk_window

        menu_options = menu_options + (('退出', None, self.QUIT),)
        self._next_action_id = self.FIRST_ID
        self.menu_actions_by_id = set()
        self.menu_options = self._add_ids_to_menu_options(list(menu_options))
        self.menu_actions_by_id = dict(self.menu_actions_by_id)
        del self._next_action_id

        self.default_menu_index = (default_menu_index or 0)
        self.window_class_name = window_class_name or "SysTrayIconPy"

        message_map = {win32gui.RegisterWindowMessage("TaskbarCreated"): self.restart,
                       win32con.WM_DESTROY : self.destroy,
                       win32con.WM_COMMAND : self.command,
                       win32con.WM_USER+20 : self.notify ,}
        # 注册窗口类。
        wc = win32gui.WNDCLASS()
        wc.hInstance = win32gui.GetModuleHandle(None)
        wc.lpszClassName = self.window_class_name
        wc.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW;
        wc.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
        wc.hbrBackground = win32con.COLOR_WINDOW
        wc.lpfnWndProc = message_map #也可以指定wndproc.
        self.classAtom = win32gui.RegisterClass(wc)

    def activation(self):
        '''激活任务栏图标，不用每次都重新创建新的托盘图标'''
        hinst = win32gui.GetModuleHandle(None)# 创建窗口。
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = win32gui.CreateWindow(self.classAtom, 
                                       self.window_class_name, 
                                       style,
                                       0, 0, 
                                       win32con.CW_USEDEFAULT, 
                                       win32con.CW_USEDEFAULT,
                                       0, 0, hinst, None)
        win32gui.UpdateWindow(self.hwnd)
        self.notify_id = None
        self.refresh(title = '软件已后台！', msg = '点击重新打开', time = 500)
        
        win32gui.PumpMessages()
        

    def refresh(self, title = '', msg = '', time = 500):
        '''刷新托盘图标
           title 标题
           msg   内容，为空的话就不显示提示
           time  提示显示时间'''
        hinst = win32gui.GetModuleHandle(None)
        if os.path.isfile(self.icon):
            icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
            hicon = win32gui.LoadImage(hinst, self.icon, win32con.IMAGE_ICON,
                                       0, 0, icon_flags)
        else: # 找不到图标文件 - 使用默认值
            hicon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)

        if self.notify_id: message = win32gui.NIM_MODIFY
        else: message = win32gui.NIM_ADD

        self.notify_id = (self.hwnd, 0, # 句柄、托盘图标ID
               win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP | win32gui.NIF_INFO,  #托盘图标可以使用的功能的标识
               win32con.WM_USER + 20, hicon, self.hover_text,  # 回调消息ID、托盘图标句柄、图标字符串
               msg, time, title,   # 提示内容、提示显示时间、提示标题
               win32gui.NIIF_INFO  # 提示用到的图标
               )
        win32gui.Shell_NotifyIcon(message, self.notify_id)

    def show_menu(self):
        '''显示右键菜单'''
        menu = win32gui.CreatePopupMenu()
        self.create_menu(menu, self.menu_options)
        
        pos = win32gui.GetCursorPos()
        win32gui.SetForegroundWindow(self.hwnd)
        win32gui.TrackPopupMenu(menu,
                                win32con.TPM_LEFTALIGN,
                                pos[0],
                                pos[1],
                                0,
                                self.hwnd,
                                None)
        win32gui.PostMessage(self.hwnd, win32con.WM_NULL, 0, 0)

    def _add_ids_to_menu_options(self, menu_options):
        result = []
        for menu_option in menu_options:
            option_text, option_icon, option_action = menu_option
            if callable(option_action) or option_action in self.SPECIAL_ACTIONS:
                self.menu_actions_by_id.add((self._next_action_id, option_action))
                result.append(menu_option + (self._next_action_id,))
            else:
                result.append((option_text,
                               option_icon,
                               self._add_ids_to_menu_options(option_action),
                               self._next_action_id))
            self._next_action_id += 1
        return result

    def restart(self, hwnd, msg, wparam, lparam):
        self.refresh()

    def destroy(self, hwnd = None, msg = None, wparam = None, lparam = None, exit = 1):
        nid = (self.hwnd, 0)
        win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, nid)
        win32gui.PostQuitMessage(0) # 终止应用程序。
        if exit and self.on_quit: self.on_quit() #需要传递自身过去时用 self.on_quit(self)
        else: self.root.deiconify()  #显示tk窗口

    def notify(self, hwnd, msg, wparam, lparam):
        '''鼠标事件'''
        if lparam==win32con.WM_LBUTTONDBLCLK:# 双击左键
            pass
        elif lparam==win32con.WM_RBUTTONUP:  # 右键弹起
            self.show_menu()
        elif lparam==win32con.WM_LBUTTONUP:  # 左键弹起
            self.destroy(exit = 0)
        return True
        """
        可能的鼠标事件：
          WM_MOUSEMOVE      #光标经过图标
          WM_LBUTTONDOWN    #左键按下
          WM_LBUTTONUP      #左键弹起
          WM_LBUTTONDBLCLK  #双击左键
          WM_RBUTTONDOWN    #右键按下
          WM_RBUTTONUP      #右键弹起
          WM_RBUTTONDBLCLK  #双击右键
          WM_MBUTTONDOWN    #滚轮按下
          WM_MBUTTONUP      #滚轮弹起
          WM_MBUTTONDBLCLK  #双击滚轮
        """
    
    def create_menu(self, menu, menu_options):
        for option_text, option_icon, option_action, option_id in menu_options[::-1]:
            if option_icon:
                option_icon = self.prep_menu_icon(option_icon)
            
            if option_id in self.menu_actions_by_id:                
                item, extras = win32gui_struct.PackMENUITEMINFO(text = option_text,
                                                                hbmpItem = option_icon,
                                                                wID = option_id)
                win32gui.InsertMenuItem(menu, 0, 1, item)
            else:
                submenu = win32gui.CreatePopupMenu()
                self.create_menu(submenu, option_action)
                item, extras = win32gui_struct.PackMENUITEMINFO(text = option_text,
                                                                hbmpItem = option_icon,
                                                                hSubMenu = submenu)
                win32gui.InsertMenuItem(menu, 0, 1, item)

    def prep_menu_icon(self, icon):
        #加载图标。
        ico_x = win32api.GetSystemMetrics(win32con.SM_CXSMICON)
        ico_y = win32api.GetSystemMetrics(win32con.SM_CYSMICON)
        hicon = win32gui.LoadImage(0, icon, win32con.IMAGE_ICON, ico_x, ico_y, win32con.LR_LOADFROMFILE)

        hdcBitmap = win32gui.CreateCompatibleDC(0)
        hdcScreen = win32gui.GetDC(0)
        hbm = win32gui.CreateCompatibleBitmap(hdcScreen, ico_x, ico_y)
        hbmOld = win32gui.SelectObject(hdcBitmap, hbm)
        brush = win32gui.GetSysColorBrush(win32con.COLOR_MENU)
        win32gui.FillRect(hdcBitmap, (0, 0, 16, 16), brush)
        win32gui.DrawIconEx(hdcBitmap, 0, 0, hicon, ico_x, ico_y, 0, 0, win32con.DI_NORMAL)
        win32gui.SelectObject(hdcBitmap, hbmOld)
        win32gui.DeleteDC(hdcBitmap)
        
        return hbm

    def command(self, hwnd, msg, wparam, lparam):
        id = win32gui.LOWORD(wparam)
        self.execute_menu_option(id)
        
    def execute_menu_option(self, id):
        menu_action = self.menu_actions_by_id[id]      
        if menu_action == self.QUIT:
            win32gui.DestroyWindow(self.hwnd)
        else:
            menu_action()

# class _Main:  #调用SysTrayIcon的Demo窗口
#     def __init__(self):
#         self.SysTrayIcon  = None  # 判断是否打开系统托盘图标

#     def main(self):
#         #tk窗口
#         self.root = tk.Tk()
#         self.root.bind("<Unmap>", lambda event: self.Hidden_window() if self.root.state() == 'iconic' else False) #窗口最小化判断，可以说是调用最重要的一步
#         self.root.protocol('WM_DELETE_WINDOW', self.exit) #点击Tk窗口关闭时直接调用s.exit，不使用默认关闭
#         self.root.resizable(0,0)  #锁定窗口大小不能改变
#         self.root.mainloop()

#     def switch_icon(self, _sysTrayIcon, icon = 'D:\\2.ico'):
#         #点击右键菜单项目会传递SysTrayIcon自身给引用的函数，所以这里的_sysTrayIcon = self.sysTrayIcon
#         #只是一个改图标的例子，不需要的可以删除此函数
#         _sysTrayIcon.icon = icon
#         _sysTrayIcon.refresh()
        
#         #气泡提示的例子
#         self.show_msg(title = '图标更换', msg = '图标更换成功！', time = 500)

#     def show_msg(self, title = '标题', msg = '内容', time = 500):
#         self.SysTrayIcon.refresh(title = title, msg = msg, time = time)

#     def Hidden_window(self, icon = 'D:\\1.ico', hover_text = "SysTrayIcon.py Demo"):
#         '''隐藏窗口至托盘区，调用SysTrayIcon的重要函数'''

#         #托盘图标右键菜单, 格式: ('name', None, callback),下面也是二级菜单的例子
#         #24行有自动添加‘退出’，不需要的可删除
#         menu_options = (('一级 菜单', None, self.switch_icon),  
#                         ('二级 菜单', None, (('更改 图标', None, self.switch_icon), )))

#         self.root.withdraw()   #隐藏tk窗口
#         if not self.SysTrayIcon: self.SysTrayIcon = SysTrayIcon(
#                                         icon,               #图标
#                                         hover_text,         #光标停留显示文字
#                                         menu_options,       #右键菜单
#                                         on_quit = self.exit,   #退出调用
#                                         tk_window = self.root, #Tk窗口
#                                         )
#         self.SysTrayIcon.activation()

#     def exit(self, _sysTrayIcon = None):
#         self.root.destroy()
#         print ('exit...')
#         os._exit(0)
# 
# if __name__ == '__main__':
#     Main = _Main()
#     Main.main()

