import time
import os
import sys
from colorama import init, Fore, Style, deinit, Cursor
from VisualizeIt_implementations.BinarySearch import BinarySearch
from VisualizeIt_implementations.BubbleSort import BubbleSort
from VisualizeIt_implementations.ImprovedBubbleSort import ImprovedBubbleSort
init()

POS = Cursor.POS()


def clrscr():
    if sys.platform != "linux":
        os.system("cls")
    else:
        os.system("clear")


class Visualizer:
    def __init__(self, algoimpl) -> None:
        self.speeds = {
            'flash': 0.03,
            'godspeed': 0.2,
            'ultra': 0.7,
            'slow': 4,
            'mid': 2,
            'fast': 1
        }
        winwidth = os.get_terminal_size()[0]
        self.algo = algoimpl
        self.initdata = self.algo.data['algorithm']
        self.type = self.initdata['type']
        self.array = self.algo.data['array']
        self.name = self.initdata['name']
        self.mainlabel = f'''{Fore.CYAN + Style.BRIGHT}{
        "VisualizeIt - Algorithms Visualized".center(winwidth)}
{Style.RESET_ALL}Currently performing {Fore.RED + Style.BRIGHT +
self.type + Style.RESET_ALL} using
{Style.BRIGHT + Fore.GREEN + self.name + Style.RESET_ALL} on
[ {Style.BRIGHT + " ".join(map(str, self.array)) + Style.RESET_ALL} ] \n
'''


class SearchVisualizer(Visualizer):
    def __init__(self, algoimpl: BinarySearch) -> None:
        super().__init__(algoimpl)
        self.algo = algoimpl
        self.data = self.algo.data

    def run(self, element: int, speed='mid'):
        clrscr()
        runner = self.algo.step_search(element)
        self.data = runner.__next__()

        # print(self.locallabel)
        found = False
        while not found:
            if self.data['found'] is True or self.data['notfound'] is True:
                found = True

            winwidth = os.get_terminal_size()[0]
            clrscr()
            start = self.data['process_data']['start']
            mid = self.data['process_data']['mid']
            end = self.data['process_data']['end']
            label = f'''{Style.BRIGHT}{
                    Fore.GREEN if self.data["searching"]
                    else Fore.RED}\tSearching{Style.RESET_ALL} for {
                    Style.BRIGHT+str(element)} in {self.algo.arr}

{Fore.RED + Style.BRIGHT + ('Start : '+ str(start)).ljust(10)
}{Fore.GREEN + Style.BRIGHT + ("Mid : "+ str(mid)).center(winwidth-18)
}{Fore.CYAN + Style.BRIGHT + ("End : " + str(end)).rjust(8) + Style.RESET_ALL}

{"Array : " + ("[" + " ".join([
    (Style.DIM + str(val) + Style.RESET_ALL) if idx < start
    else (Fore.RED + Style.BRIGHT + str(val) + Style.RESET_ALL) if idx==start
    else (Fore.GREEN + Style.BRIGHT + str(val) + Style.RESET_ALL) if idx == mid
    else (Fore.CYAN + Style.BRIGHT + str(val) + Style.RESET_ALL) if idx == end
    else (Style.BRIGHT + str(val) + Style.RESET_ALL)
    for idx,val in enumerate(self.algo.arr)])+"]" + Style.RESET_ALL)}

{Style.BRIGHT + Fore.LIGHTRED_EX
+ self.data['msg'].center(winwidth) + Style.RESET_ALL}
'''
            print(POS + self.mainlabel + label)
            time.sleep(1*self.speeds[speed])
            try:
                self.data = runner.__next__()
            except StopIteration:
                pass
        deinit()


class SortVisualizer(Visualizer):
    def __init__(self, algoimpl: BubbleSort) -> None:
        super().__init__(algoimpl)
        self.algo = algoimpl
        self.data = self.algo.data

    def run(self, speed='mid'):
        clrscr()
        runner = self.algo.sort()
        self.data = runner.__next__()
        winwidth_old = os.get_terminal_size()[0]
        sorted_arr = False
        while not sorted_arr:
            if self.data['sorted'] is True:
                sorted_arr = True

            winwidth_new = os.get_terminal_size()[0]
            comparing_idx = self.data['comparing_data'].values()
            swapping_idx = self.data['swapping_data'].values()
            pass_number = self.data['pass']
            fixed = self.data.get('fixed', len(self.algo.arr))
            visual_fixed = pass_number-1
            comparisons = self.data['comparisons']
            swaps = self.data['swaps']
            winwidth = winwidth_new
            if sorted_arr:
                comparing_idx = []
                swapping_idx = []
            if winwidth_new != winwidth_old:
                clrscr()

            label = f'''
{Style.BRIGHT}
{("Total Passes : "+ str(pass_number)).center(winwidth//2)}{
("Fixed Elements : " + str(visual_fixed)).center(winwidth//2)}
{("Comparisons : " + str(comparisons)).center(winwidth//2)}{
("Swaps : " + str(swaps)).center(winwidth//2)}
{Style.BRIGHT}{
Fore.GREEN if self.data["comparing"] else Fore.RED
}{"COMPARING".center(winwidth)}{
Style.RESET_ALL}
{Style.BRIGHT}{
Fore.LIGHTGREEN_EX if self.data['swapping'] else Fore.LIGHTRED_EX
}{"SWAPPING".center(winwidth)}{
Style.RESET_ALL}

{"Array : " + ("[" + " ".join([
    (Style.DIM + str(val) + Style.RESET_ALL)
    if (idx not in comparing_idx) and
    (idx not in swapping_idx) and (idx < fixed
    )
    else (Fore.RED + Style.BRIGHT + str(val) + Style.RESET_ALL)
    if self.data['comparing'] and (idx in comparing_idx)
    else (Fore.GREEN + Style.BRIGHT + str(val) + Style.RESET_ALL)
    if self.data['swapping'] and (idx in swapping_idx)
    else (Style.BRIGHT + Fore.LIGHTCYAN_EX + str(val) + Style.RESET_ALL)
    if idx > fixed
    else (Style.DIM + str(val) + Style.RESET_ALL)
    for idx,val in enumerate(self.data['arr'])
    ])+"]" + Style.RESET_ALL)}

{Style.BRIGHT + Fore.LIGHTRED_EX
+ self.data['msg'].center(winwidth) + Style.RESET_ALL}
'''
            print(POS + self.mainlabel + label)
            time.sleep(1*self.speeds[speed])
            winwidth_old = winwidth_new
            try:
                self.data = runner.__next__()
            except StopIteration:
                pass
        deinit()


class ImprovedSortVisualizer(Visualizer):
    def __init__(self, algoimpl: ImprovedBubbleSort) -> None:
        super().__init__(algoimpl)
        self.algo = algoimpl
        self.data = self.algo.data

    def run(self, speed='mid'):
        clrscr()
        runner = self.algo.sort()
        self.data = runner.__next__()
        winwidth_old = os.get_terminal_size()[0]
        sorted_arr = False
        while not sorted_arr:
            if self.data['sorted'] is True:
                sorted_arr = True

            winwidth_new = os.get_terminal_size()[0]
            comparing_idx = self.data['comparing_data'].values()
            swapping_idx = self.data['swapping_data'].values()
            pass_number = self.data['pass']
            fixed = self.data.get('fixed', len(self.algo.arr))
            visual_fixed = pass_number-1
            comparisons = self.data['comparisons']
            swaps = self.data['swaps']
            winwidth = winwidth_new
            if sorted_arr:
                comparing_idx = []
                swapping_idx = []
            if winwidth_new != winwidth_old:
                clrscr()

            label = f'''
{Style.BRIGHT}
{("Total Passes : "+ str(pass_number)).center(winwidth//2)}{
("Fixed Elements : " + str(visual_fixed)).center(winwidth//2)}
{("Comparisons : " + str(comparisons)).center(winwidth//2)}{
("Swaps : " + str(swaps)).center(winwidth//2)}
{Style.BRIGHT}{
Fore.GREEN if self.data["comparing"] else Fore.RED
}{"COMPARING".center(winwidth)}{
Style.RESET_ALL}
{Style.BRIGHT}{
Fore.LIGHTGREEN_EX if self.data['swapping'] else Fore.LIGHTRED_EX
}{"SWAPPING".center(winwidth)}{
Style.RESET_ALL}

{"Array : " + ("[" + " ".join([
    (Style.DIM + str(val) + Style.RESET_ALL)
    if (idx not in comparing_idx) and
    (idx not in swapping_idx) and (idx < fixed
    )
    else (Fore.RED + Style.BRIGHT + str(val) + Style.RESET_ALL)
    if self.data['comparing'] and (idx in comparing_idx)
    else (Fore.GREEN + Style.BRIGHT + str(val) + Style.RESET_ALL)
    if self.data['swapping'] and (idx in swapping_idx)
    else (Style.BRIGHT + Fore.LIGHTCYAN_EX + str(val) + Style.RESET_ALL)
    if idx > fixed
    else (Style.DIM + str(val) + Style.RESET_ALL)
    for idx,val in enumerate(self.data['arr'])
    ])+"]" + Style.RESET_ALL)}

{Style.BRIGHT + Fore.LIGHTRED_EX
+ self.data['msg'].center(winwidth) + Style.RESET_ALL}
'''
            print(POS + self.mainlabel + label)
            time.sleep(1*self.speeds[speed])
            winwidth_old = winwidth_new
            try:
                self.data = runner.__next__()
            except StopIteration:
                pass
        deinit()
