
package_weight = 0
max_weight = 20
packages_sent = 0
total_weight = 0
unused_space = 0
count = 1
max_unused_weight = 0
package_with_max_unused_weight = 0

#Ask user the number of items to be sent
max_items = int(input("How many items would you like to ship? : "))

#Ask user to put the weight of each item and count the items
for item in range(max_items):
    while True:
        item_weight = int(input(f"What is the weight of the item {item+1}? :  "))
        if item_weight >= 1 and item_weight <= 10:  #(revert for error free) while True quiting9
           break
        else:
             print("\nInvailid weight\nMinimum weight is 1\nMax weight is 10\nTry again :")
                    
    if item_weight <= 0: # breaking out the look when pressing 0 (out of four loop)
        print("Invailid input try again")
        break
    package_weight += item_weight # each item is added in to packets
    if package_weight > max_weight:
        print("sending the packet")
        packages_sent += 1 #count the packages
        if max_unused_weight < max_weight - (package_weight - item_weight): # curent package = 20 - (package -item)
             package_with_max_unused_weight = packages_sent  # witch package has most unused space
             max_unused_weight = max_weight - (package_weight - item_weight) # give and stor info what was the max unused capacity
             print(max_unused_weight)
        total_weight += package_weight - item_weight #count the packet without the item that make it overwheit 
        package_weight = item_weight  #if item doesent fit in last box, transfer to next box
    elif package_weight == max_weight:
        print("Sending the packet")
        packages_sent += 1
        total_weight += package_weight
        package_weight = 0
if package_weight > 0: # we check to see if we have any packet unsent for the las items without reaching 20kg
    print("Sending the packet")
    packages_sent += 1
    print(id(packages_sent))
    if max_unused_weight < max_weight - package_weight : # curent package = 20 - (package -item)
             package_with_max_unused_weight = packages_sent  # witch package has most unused space
             max_unused_weight = max_weight - package_weight #(no need to - item weight as is last box)
    total_weight += package_weight

if item_weight < 0:
    print("Maximum number reached")

unused_space = packages_sent * max_weight - total_weight #find the unused spaces in the box
print("\nOverall informations\n")

print(f"Items total Weight: {total_weight}\npackages sent: {packages_sent}\nTotal 'unused' capacity: {unused_space}\npackage max unused space: {package_with_max_unused_weight}\nmax unused pace in the packet: {max_unused_weight}" )


  
            #    print("Not enough founds")
            #    breakbalance