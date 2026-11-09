from dolphin import gui, event, utils
from external import external_utils as ex
import os
from time import sleep

shm_auto_cancel = ex.SharedMemoryBlock.create('config_ini_cancel', buffer_size=256)

@event.on_timertick
def cancel() -> None:
    global shm_auto_cancel
    if shm_auto_cancel.read_text() == 'cancel_now':
        gui.add_osd_message(f'configuration saved to {utils.get_script_dir()}\\FrameDumps\\config.ini')
        sleep(0.3)
        utils.cancel_script(utils.get_script_name())

def main() -> None:
    shm_framedump = ex.SharedMemoryWriter(name='framedump_dir', buffer_size=256)
    shm_framedump.write_text(f'{utils.get_script_dir()}\\FrameDumps')
    shm_utils = ex.SharedMemoryWriter(name='framedump_utils', buffer_size=256)
    shm_utils.write_text(f'{utils.get_script_dir()}\\external\\config_ini_utils')
    gui.add_osd_message('Script started')
    ex.start_external_script(os.path.join(utils.get_script_dir(), 'external', 'config_ini_window.py'))

if __name__ == '__main__':
    main()