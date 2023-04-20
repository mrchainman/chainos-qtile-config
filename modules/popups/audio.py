from pulsectl import Pulse

with Pulse() as pulse:
    # Create empty dict
    devices = {}
    # Add devices to dict
    for i in pulse.sink_list():
                 devices["name"] = i.proplist['device.product.name']
                 devices["sink"] = i

    # When name is saved as chosen it can be set as default here
    pulse.sink_default_set(devices[chosen])


    
pulse.volume_set_all_chans(devices[chosen], 0.1)
pulse.volume_get_all_chans(devices[chosen])
