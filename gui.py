import pygame
import pygame_menu

from functools import partial

import pygame_menu.themes

from fcfs import fcfs
from process import Process
from SJF import sjf_non_preemptive, sjf_preemptive

from menu import * 

dummy_process = [Process(1,0,7), Process(2, 2, 4), Process(3, 4, 1), Process(4, 5, 4)]

# placeholder
def sentinel():
    return [(0, 1, 2)]

class GUIInterface():
    
    def __init__(self, scheduler_window):
        self._menu = scheduler_window
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)
        self.screen = DISPLAY
        self._construct_gantt_chart(mode=fcfs, processes=dummy_process)

    def reset(self):
        self._menu.full_reset()
        self._menu.clear()

    def start_update_loop(self, events):

        self._menu.update(events)
        # Rendering happens here
        for process, pid in self._process_rect_list:
            pygame.draw.rect(self.screen, WHITE, process, 2)
            self.screen.blit(
                pid,
                (process.x + (process.width - pid.get_width()) / 2, process.y + (process.height - pid.get_height()) / 2)
            )
        dt = self.clock.tick(FPS) / 1000



    def _construct_gantt_chart(self, data=None, mode=fcfs, processes: list[Process]=[]):
        y_coordinate = HEIGHT / 3
        rectangle_width = WIDTH - 60

        processes = Process.reset_all(processes)
        rendering_list = mode(processes)
        total_time = max([process[2] for process in rendering_list])
        chart_unit_time = rectangle_width / total_time

        self._process_rect_list = []
        last_process_end = 30
        for process in rendering_list:
            process_width = process[1] * chart_unit_time
            self._process_rect_list.append(
                (
                    pygame.rect.Rect(last_process_end, y_coordinate, process_width, 30),
                    self.font.render(f"P:{process[0]}", True, WHITE)
                )
            )

            last_process_end = last_process_end - 2 + process_width
    