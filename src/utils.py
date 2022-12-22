
from psychopy import visual, core, sound, event

def wait_for_click(win, visual):
    """
    Waits for a keypress to be pressed

    :param win: window projected on monitor
    :param visual: visual to be displayed
    :returns: key pressed
    """
    click = None
    while click == None:
        visual.draw()
        win.flip()
        click = event.waitKeys()
    if click[0] == 'Esc':
        win.close()
        core.quit()
    return click


def draw_visual(window, visual, time):
    """
    Draws a visual image onto the window

    :param window: window projected on monitor
    :param visual: visual to be displayed
    :param time: time visual is displayed (s)
    :returns: shows visual on window
    """
    
    visual.draw()
    window.flip()
    core.wait(time)

def convert_db_to_vol(this_vol):
    """
    Returns the volume value of a dB

    :param this_vol: the volume value (in dB)
    :returns: the volume value as a float between 0 and 1
    """
    return ((0.34/0.1)/(10**(111.8/20)))*(10**(this_vol/20))

def get_audio(amp, freq, time):
    """
    Returns a sound object given the amplitude, frequency, and time
    
    :param amp: Amplitude value (in dB)
    :param freq: Frequency value (in Hz)
    :param time: Time value (in s)
    :returns: sound object in Psychopy
    """
    
    return sound.Sound(value=freq, secs=time, volume=convert_db_to_vol(amp), autoLog=True)

def get_keypress(win):
    keys = event.getKeys()
    if keys and keys[0] == 'Esc':
        win.close()
        core.quit()
    else: 
        return False