# import sqlite3

# conn = sqlite3.connect('barter.db')
# print("Opened db succesfully!")

# conn.execute('''CREATE TABLE ASSET_CATEGORY (ASSET_CAT_ID INT PRIMARY KEY NOT NULL, ASSET_CATEGORY_NAME TEXT NOT NULL)''')
# conn.execute('''CREATE TABLE ASSET (ASSET_ID INT PRIMARY KEY NOT NULL, 
#                         ASSET_CAT_ID  INT,
#                         ASSET_NAME CHAR(100),
#                         ASSET_AUTHOR CHAR(50),
#                         ASSET_COMPANY CHAR(100))''')
# conn.execute('''CREATE TABLE USER (USER_ID INT PRIMARY KEY NOT NULL,
#                         USER_NAME CHAR(50),
#                         USER_EMAIL CHAR(50))''')
# conn.execute('''CREATE TABLE  MAP_USER_ASSET_OWNERSHIP_WISH (USER_ID INT, 
#                                                 ASSET_ID INT,
#                                                 ISOWNED BOOLEAN,
#                                                 ISWISH BOOLEAN)''')
# print("Opened db succesfully!")
# conn.close()

import sqlite3

#########################################################################################
###   FUNCTION: createBarterDB                                                        ###
###   USE: Create barter.db                                                           ###
###   RETURN: (phase1) ? 0: conn                                                      ###
#########################################################################################
def createBarterDB():
    print('>>inside createBarterDB function')
    conn = sqlite3.connect('barter.db')
    print("Opened db succesfully!")
    return conn

#########################################################################################
###   FUNCTION: createDDLBarter                                                       ###
###   USE: DDLs for the Project.                                                      ###
###   RETURN: (phase1) ? 0: 0/1                                                       ###
#########################################################################################
def createDDLBarter(conn)
    print('>>inside createDDLBarter function')
    conn.execute('''CREATE TABLE ASSET_CATEGORY (ASSET_CAT_ID INT PRIMARY KEY NOT NULL, ASSET_CATEGORY_NAME TEXT NOT NULL)''')
    conn.execute('''CREATE TABLE ASSET (ASSET_ID INT PRIMARY KEY NOT NULL, 
                            ASSET_CAT_ID  INT,
                            ASSET_NAME CHAR(100),
                            ASSET_AUTHOR CHAR(50),
                            ASSET_COMPANY CHAR(100))''')
    conn.execute('''CREATE TABLE USER (USER_ID INT PRIMARY KEY NOT NULL,
                            USER_NAME CHAR(50),
                            USER_PASSWORD CHAR(50),
                            USER_EMAIL CHAR(50))''')
    conn.execute('''CREATE TABLE  MAP_USER_ASSET_OWNERSHIP_WISH (USER_ID INT, 
                                                    ASSET_ID INT,
                                                    ISOWNED BOOLEAN,
                                                    ISWISH BOOLEAN)''')
    print("Created tables and structure succesfully!")
    return 0

#########################################################################################
###   FUNCTION: createUser                                                            ###
###   USE: User details insertion in DB.                                              ###
###   RETURN: (phase1) ? 0: UserID                                                    ###
#########################################################################################

def createUser(conn):
    print('>>inside createUser function')
    varUserId = testUserId # TODO: Should have userid dynamically generated
    varUserName = testUserName
    varEmail = testEmail
    varPwd = testUserName # TODO : Encrypt password before storing in db
    UserProfileData = [varUserId, varUserName, varEmail, varPwd] #User array, TODO : should come from UI later.

    sql = ''' INSERT INTO USER(USER_ID,USER_NAME,USER_EMAIL, USER_PASSWORD)
              VALUES(?,?,?) '''
    print(sql)
    cur = conn.cursor()
    cur.execute(sql, UserProfileData)
    return 0; # TODO: return the user id created dynamically

#########################################################################################
###   FUNCTION: UserCreation                                                          ###
###   USE: User details generated for project                                         ###
###   RETURN: (phase1) ? 0: UserID                                                    ###
#########################################################################################
def UserCreation(conn):
    var userID = 0
    print('>>inside UserCreation function')
    userId = createUser(conn)
    return userId

#########################################################################################
###   FUNCTION: Login                                                                 ###
###   USE: User details generated for project, Will move to UI                        ###
###   RETURN: (phase1) ? 0: UserID                                                    ###
#########################################################################################
def UserLogin(userName, password):
    cur = conn.cursor()
    AuthSql = ''' SELECT USER_PASSWORD from USER WHERE USER USER_NAME = ?'''
    varAuth = cur.execute(unmSql, userName)
    if(PHASEONE):
        userName = password
    else:
        password=varAuth
        return 0
        print('Login granted...')

#########################################################################################
###   FUNCTION: addOwnershiptoAsset                                                   ###
###   USE: Adding the owned Asset from UI     - Insert to asset and map table         ###
###   RETURN: (phase1) ? 0: Asset_id                                                  ###
#########################################################################################
def addOwnershiptoAsset():
    # Create the column for insertion -> 
        # Asset table
            # cat_id - Get from selected category
            # asset_id (generate new id - A_n {n = 1,2,3,4 ....}).
            # asset_name - Title of asset, Name of Asset - comes from UI.
            # asset_author - Owner entered from UI - mandatory field.
            # asset_company - Publisher, Manufacturer .. from UI - optional detail.
            # Description - Other details
        # Asset_user_mapping_table
            # user_id - Pull from logged in user - UI
            # asset_id - same as Asset_table->asset_id added above.
            # isOwned - Y 
            # isWished - N (default)
            # Quoted value - User input (quote from user on product) from UI - A backend value use to show suggestions.
    # Add ownership
        # insert operation to mapping table with 
    

#########################################################################################
###   FUNCTION: main                                                                  ###
###   USE: Temp function to handle the complete flow                                  ###
###   RETURN: (phase1) ? 0: 0/1                                                       ###
#########################################################################################
def main():
    # run ones
    conn = createBarterDB()
    createDDLBarter(conn)
    # run ones end

    UserCreation()
    return 0

    

# Modules lising ..
    # UserMgr: User Management ( userName == password, User profile creation)
    # Validation : Deadlock prevention ( hold assets while in use).
    # Blacklisting : Preventing the illegal or inhumane exchanges.
    # AssetMgr: Asset Manager, managing 
    # OwnershipMgr: All the operations related to ownership management.
    # WishMgr: All the operations related to wish management.
    # ExchangeMgr: All the operation related to exchange and transaction management and value mapping for default view.