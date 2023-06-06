import random

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]
    # YOUR CODE GOES HERE
    
    new_friend = []
    for i in range(1, len(friends)): # Turning the raw read into a set of tuples that are easier to work with
        new_friend = friends[i].split(" ")
        friends[i] = new_friend[:]
        
    x = 0
    y = 0
    cols = []
    rows = [0, cols[:]]
    for i in range(int(friends[0])): # Turns Network into a 2D array
        rows[0] = i
        rows[1] = cols[:]
        network.append(rows[:])
        
    for i in range(1, len(friends)): # Appending the friends to the Network
        x = int(friends[i][0])
        y = int(friends[i][1])
        network[y][1].append(x)
        network[x][1].append(y)
    
        
    return network

def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    # YOUR CODE GOES HERE
    x = 0
    y = 0
    # FOR TESTING PURPOSES
    computations = 0
    while x < len(network[user1][1]) and y < len(network[user2][1]):
        computations += 1
        if network[user1][1][x] == network[user2][1][y]:
            common.append(network[user1][1][x])
            x += 1
            y += 1
        elif (network[user1][1][x] > network[user2][1][y]):
            y += 1
        else:
            x += 1
            
    # SPEED TESTING
    # print("USER1", len(network[user1][1]))
    # print("USER2", len(network[user2][1]))
    # print("NUMBER OF COMPUTATIONS:", computations)
    # RUNS n1 + 1 or n2 + 1 times in best case 
    # RUNS n1 + n2 times in worst case (doesn't require log n,
    # as the friend list is already sorted from the create_network() function)
    return common

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour(does this mean friend?) in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    # YOUR CODE GOES HERE
    most_friends = [0, 0] # INDEX, VALUE
    place_holder = 0
    for i in range(len(network)):
        if i not in network[user][1] and i != user:
            place_holder = len(getCommonFriends(user, i, network))
            if place_holder > most_friends[1]:
                most_friends[1] = place_holder
                most_friends[0] = i
                
    if most_friends[0] == 0:
        return None
    else:
        return most_friends[0]
            

    


def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE
    number_users = 0
    for i in range(len(network)):
        if len(network[i][1]) >= k:
            number_users += 1

    return number_users
        
 

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    # YOUR CODE GOES HERE
    max_friends = 0
    for i in range(len(network)):
        if len(network[i][1]) > max_friends:
            max_friends = len(network[i][1])
    return max_friends
    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    # YOUR CODE GOES HERE
    maxi = maximum_num_friends(network)
    for i in range(len(network)):
        if len(network[i][1]) == maxi:
            max_friends.append(i)
            
    return max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    # YOUR CODE GOES HERE
    summ = 0
    for i in range(len(network)):
        summ += len(network[i][1])

    summ = summ/len(network)

    return summ
    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    # YOUR CODE GOES HERE
    for i in range(len(network)):
        if len(network[i][1]) == len(network) - 1:
            return True
    return False


####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name

def get_raw_uid():
    """ None -> int, None
    Takes the raw input from the user and varifies that it is a usable UID
    No preconditions
    """
    UID = 0
    try:
        UID = int(input("Please Enter a Valid User ID:"))
        return UID
    except ValueError:
        print("Error. Please Enter an Integer")
    

def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    # YOUR CODE GOES HERE
    verification_array = []
    for i in range(len(network)):
        verification_array.append(i)
    
    uid = "s"
    while uid not in verification_array:
        # print("User ID must be valid.")
        uid = get_raw_uid()
    
    return uid
    

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    
