#!/usr/bin/env python

def EnterNew(self):
 
	ings = []
 
	recipename = ''
 
        recipesource = ''
 
        recipeserves = ''
 
        instructions = ''
 
        lastid = 0
 
        resp = raw_input('Enter Recipe Title (Blank line to exit) -> ')
 
        if resp != '' :  # continue
 
            if string.find(resp,"'"):
 
                recipename = resp.replace("'","\'")
 
            else:
 
                recipename = resp
 
            print "RecipeName will be %s" % recipename
 
            resp = raw_input('Enter Recipe Source -> ')
 
            if string.find(resp,"'"):
 
                recipesource = resp.replace("'","\'")
 
            else:
 
                recipesource = resp
 
            resp = raw_input('Enter number of servings -> ')
 
            if string.find(resp,"'"):
 
                recipeserves = resp.replace("'","\'")
 
            else:
 
                recipeserves = resp
 
            print 'Now we will enter the ingredient list.'
 
            cont = True
 
            while cont == True:
 
                ing = raw_input('Enter Ingredient ("0" to exit) -> ')
 
                if ing != '0':
 
                    ings.append(ing)
 
                else:
 
                    cont = False
 
            resp = raw_input('Enter Instructions -> ')
 
            instructions = resp
 
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
 
            print "Here's what we have so far"
 
            print "Title: %s" % recipename
 
            print "Source: %s" % recipesource
 
            print "Serves: %s" % recipeserves
 
            print "Ingredients:"
 
            for x in ings:
 
                print x
 
            print "Instructions: %s" % instructions
 
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
 
            resp = raw_input("OK to save? (Y/n) -> ")
 
            if string.upper(resp) != 'N':
 
                connection=apsw.Connection("cookbook.db3")
 
                cursor=connection.cursor()
 
                # Write the Recipe Record
 
                sql = 'INSERT INTO Recipes (name,servings,source) VALUES ("%s","%s","%s")' %(recipename,recipeserves,recipesource)
 
                cursor.execute(sql)
 
                # Get the new Recipe pkID
 
                sql = "SELECT last_insert_rowid()"
 
                cursor.execute(sql)
 
                for x in cursor.execute(sql):
 
                    lastid = x[0]
 
                    print "last id = %s" % lastid
 
                # Write the Instruction Record
 
                for x in ings:
 
                    sql = 'INSERT INTO Ingredients (recipeID,ingredients) VALUES (%s,"%s")' % (lastid,x)
 
                    cursor.execute(sql)
 
                # Write the Ingredients records
 
                sql = 'INSERT INTO Instructions (recipeID,instructions) VALUES( %s,"%s")' %(lastid,instructions)
 
                cursor.execute(sql)
 
                # Prompt the user that we are done
 
                print 'Done'
 
            else:
 
                print 'Save aborted'
