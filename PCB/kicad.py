# Most of the code contained in this file can be attributed to Alan Sameth https://github.com/AlanSamet/KiCadExtensions

import pcbnew
pcb = pcbnew.GetBoard()

def mm_to_nm(v):
    return int(v * 1000000)
def nm_to_mm(v):
    return v / 1000000.0

def get_component(name):
    return pcb.FindFootprintByReference(name)

# Places component_to_move relative to reference_component_name with supplied x and y.
# Example, moves footprint D2 19.05mm on the x axis and aligns on y with D1: 
# place_component_relative_mm('D1', 'D2', 19.05, 0)
#
# set suppress_refresh=True when used in a loop
def place_component_relative_mm(reference_component_name, component_to_move, relative_x, relative_y, suppress_refresh = False):
    a = get_component(reference_component_name)
    b = get_component(component_to_move)

    pos_a = a.GetPosition()
    b.SetPosition(pcbnew.wxPoint(pos_a[0] + mm_to_nm(relative_x), pos_a[1] + mm_to_nm(relative_y)))
    if not suppress_refresh:
        pcbnew.Refresh()

# Same idea as above, only you can provide a list of components.
# Useful for evenly spacing a list of components
#
# Example usage, placing 8 Diodes 19.05mm apart:
# place_components_relative_mm('D1 D2 D3 D4 D5 D6 D7 D8'.split(), 19.05, 0)
#
# This is equivalent to above and much nicer to type:
# place_components_relative_mm(range(1,9), 19.05, 0, ref='D')
# 
# You can also set rev=True which will reverse the order of list and uses the last in the list as the first reference point.
# So, instead of D1 D2 D3 D4 D5 D6 D7 D8 it would be D8 D7 D6 D5 D4 D3 D2 D1
def place_components_relative_mm(components_list, relative_x, relative_y, suppress_refresh=False, ref="", rev=False):
    comps = []
    if ref != "":
        for i in list(components_list):
            comps.append(f"{str(ref)}{str(i)}")
    if rev:
        comps.reverse()
    for i in range(len(comps)-1):
        place_component_relative_mm(comps[i], comps[i+1], relative_x, relative_y, True)
    if not suppress_refresh:
        pcbnew.Refresh()