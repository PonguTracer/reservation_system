riders_per_ride = 3  # Num riders per ride to dispatch

line = []  # The line of riders
num_vips = 0  # Track number of VIPs at front of line

menu = ('(1) Reserve place in line.\n'  # Add rider to line
        '(2) Reserve place in VIP line.\n'  # Add VIP
        '(3) Dispatch riders.\n'  # Dispatch next ride car
        '(4) Print riders.\n'
        '(5) Exit.\n\n')

user_input = input(menu).strip().lower()

while user_input != '5':
    if user_input == '1':  # Add rider
        name = input('Enter name:').strip().lower()
        line.append(name)  # Append the name to the end of the line

    elif user_input == '2':  # Add VIP
        print('Add new VIP')
        name = input('Enter name: ').strip().lower()
        # Insert the VIP into the line at position num_vips
        line.insert(num_vips, name)
        num_vips += 1  # Increment num_vips

    elif user_input == '3':  # Dispatch ride
        print('Dispatching riders')
        if len(line) >= riders_per_ride:
            # Get the first riders_per_ride riders
            riders_to_dispatch = line[:riders_per_ride]
            # Remove dispatched riders from the front of the line
            line = line[riders_per_ride:]

            # Check if there were VIPs in the dispatched group
            vip_count = sum(
                1 for name in riders_to_dispatch if name in line[:num_vips])
            num_vips -= vip_count
        else:
            print("Not enough riders to dispatch")

    elif user_input == '4':  # Print riders waiting in line
        print('{} person(s) waiting:'.format(len(line)), line)

    else:
        print('Unknown menu option')

    user_input = input('Enter command: ').strip().lower()
