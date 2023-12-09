def numRescueBoats( people, limit: int) -> int:
        people.sort()

        left = 0        # Pointer pointing to the lightest person
        right = len(people) - 1  # Pointer pointing to the heaviest person
        boats = 0       # Count of boats needed

    # Use a two-pointer approach to find pairs of people to fill the boat
        while left <= right:
        # If the sum of weights is within the limit, both people can fit on the boat
            if people[left] + people[right] <= limit:
                left += 1
        
        # In any case, the heaviest person must be on the boat
            right -= 1

        # Increment the count of boats
            boats += 1

        return boats
