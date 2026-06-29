class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # have a list of tuples from 1st position to last with speeds
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        # we always have 1 fleet at least
        fleets = 1

        # time left for 1st car to finish,
        time_left_fleet_lead = (target - pair[0][0]) / pair[0][1]

        for i in range(1, len(pair)):
            current_car_time_left = (target - pair[i][0]) / pair[i][1]

            # will the current car reach to the fleet lead?
            if time_left_fleet_lead >= current_car_time_left:
                continue # no new fleet
            else:
                fleets += 1 # new fleet found and counted
                time_left_fleet_lead = current_car_time_left # new fleet lead


        return fleets