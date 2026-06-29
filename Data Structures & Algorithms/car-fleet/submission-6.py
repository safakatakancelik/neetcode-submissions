class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:        
        # Have an ordered list of tuples with positions and speeds for each car
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        # First car is the first fleet lead
        fleet_lead = pair[0]

        # Start counting the fleets
        fleets = 1

        # Calculate when the fleet lead will finish
        time_left_fleet_lead = (target - fleet_lead[0]) / fleet_lead[1]

        for i in range(1, len(pair)):
            # Calculate when the current car will finish
            current_car_time_left = (target - pair[i][0]) / pair[i][1]

            # Calculate if the current car join the fleet
            if time_left_fleet_lead >= current_car_time_left: # yes
                continue # Current car will join the fleet
            else: # no
                fleets += 1 # new fleet counted
                time_left_fleet_lead = current_car_time_left # new fleet lead


        return fleets