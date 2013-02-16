#!/usr/bin/python
#------------------------------------------------------
# Cookbook.py
# Created for Beginning Programming Using Python #8
# and Full Circle Magazine
#------------------------------------------------------

import apsw
import string
import webbrowser

class Cookbook:

    def __init__(self):
        global connection
        global cursor
        self.totalcount = 0
        connection=apsw.Connection("cookbook.db3")
        cursor=connection.cursor()
        
    def PrintAllRecipes(self):
        print '%s %s %s %s' %('Item'.ljust(5),'Name'.ljust(30),'Serves'.ljust(20),'Source'.ljust(30))
        print '--------------------------------------------------------------------------------------'
        sql = 'SELECT * FROM Recipes'
        cntr = 0
        for x in cursor.execute(sql):
            cntr += 1
            print '%s %s %s %s' %(str(x[0]).rjust(5),x[1].ljust(30),x[2].ljust(20),x[3].ljust(30))
        print '--------------------------------------------------------------------------------------'
        self.totalcount = cntr
        
    def SearchForRecipe(self):
        # print the search menu
        print '-------------------------------'
        print ' Search in'
        print '-------------------------------'
        print ' 1 - Recipe Name'
        print ' 2 - Recipe Source'
        print ' 3 - Ingredients'
        print ' 4 - Exit'
        searchin = raw_input('Enter Search Type -> ')
        if searchin != '4':
            if searchin == '1':
                search = 'Recipe Name'
            elif searchin == '2':
                search = 'Recipe Source'
            elif searchin == '3':
                search = 'Ingredients'
            parm = searchin
            response = raw_input('Search for what in %s (blank to exit) -> ' % search)
            if parm == '1': # Recipe Name
                sql = "SELECT pkid,name,source,servings FROM Recipes WHERE name like '%%%s%%'" %response
            elif parm == '2': # Recipe Source
                sql = "SELECT pkid,name,source,servings FROM Recipes WHERE source like '%%%s%%'" %response
            elif parm == '3': # Ingredients
                sql = "SELECT r.pkid,r.name,r.servings,r.source,i.ingredients FROM Recipes r Left Join ingredients i on (r.pkid = i.recipeid) WHERE i.ingredients like '%%%s%%' GROUP BY r.pkid" %response
            try:
                if parm == '3':
                    print '%s %s %s %s %s' %('Item'.ljust(5),'Name'.ljust(30),'Serves'.ljust(20),'Source'.ljust(30),'Ingredient'.ljust(30))
                    print '----------------------------------------------------------------------------------------------------------------------------'
                else:
                    print '%s %s %s %s' %('Item'.ljust(5),'Name'.ljust(30),'Serves'.ljust(20),'Source'.ljust(30))
                    print '--------------------------------------------------------------------------------------'
                for x in cursor.execute(sql):
                    if parm == '3':
                        print '%s %s %s %s %s' %(str(x[0]).rjust(5),x[1].ljust(30),x[2].ljust(20),x[3].ljust(30),x[4].ljust(30))
                    else:
                        print '%s %s %s %s' %(str(x[0]).rjust(5),x[1].ljust(30),x[3].ljust(20),x[2].ljust(30))
            except:
                print 'An Error Occured'
            print '--------------------------------------------------------------------------------------'
            inkey = raw_input('Press a key')
    def PrintSingleRecipe(self,which):
        sql = 'SELECT * FROM Recipes WHERE pkID = %s' % str(which)
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        for x in cursor.execute(sql):
            recipeid =x[0]
            print "Title: " + x[1]
            print "Serves: " + x[2]
            print "Source: " + x[3]
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        sql = 'SELECT * FROM Ingredients WHERE RecipeID = %s' % recipeid
        print 'Ingredient List:'
        for x in cursor.execute(sql):
            print x[1]
        print ''
        print 'Instructions:'
        sql = 'SELECT * FROM Instructions WHERE RecipeID = %s' % recipeid
        for x in cursor.execute(sql):
            print x[1]
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        resp = raw_input('Press A Key -> ')
    def DeleteRecipe(self,which):
        resp = raw_input('Are You SURE you want to Delete this record? (Y/n) -> ')
        if string.upper(resp) == 'Y':
            connection=apsw.Connection("cookbook.db3")
            cursor=connection.cursor()
            sql = "DELETE FROM Recipes WHERE pkID = %s" % str(which)
            cursor.execute(sql)
            sql = "DELETE FROM Instructions WHERE recipeID = %s" % str(which)
            cursor.execute(sql)
            sql = "DELETE FROM Ingredients WHERE recipeID = %s" % str(which)
            cursor.execute(sql)
            print "Recipe information DELETED"
            resp = raw_input('Press A Key -> ')
        else:
            print "Delete Aborted - Returning to menu"
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
    def PrintOut(self,which):
        #pass
        fi = open('recipeprint.html','w')
        sql = "SELECT * FROM Recipes WHERE pkID = %s" % which
        for x in cursor.execute(sql):
            RecipeName = x[1]
            RecipeSource = x[3]
            RecipeServings = x[2]
        fi.write("<H1>%s</H1>" % RecipeName)
        fi.write("<H2>Source: %s</H2>" % RecipeSource)
        fi.write("<H2>Servings: %s</H2>" % RecipeServings)
        fi.write("<H3> Ingredient List: </H3>")
        sql = 'SELECT * FROM Ingredients WHERE RecipeID = %s' % which
        for x in cursor.execute(sql):
            fi.write("<li>%s</li>" % x[1])
        fi.write("<H3>Instructions:</H3>")
        sql = 'SELECT * FROM Instructions WHERE RecipeID = %s' % which
        for x in cursor.execute(sql):
            fi.write(x[1])
        fi.close()
        webbrowser.open('recipeprint.html')
        print "Done"
def Menu():
    cbk = Cookbook() # Initialize the class
    loop = True
    while loop == True:
        print '==================================================='
        print '               RECIPE DATABASE'
        print '==================================================='
        print ' 1 - Show All Recipes'
        print ' 2 - Search for a recipe'
        print ' 3 - Show a Recipe'
        print ' 4 - Delete a recipe'
        print ' 5 - Add a recipe'
        print ' 6 - Print a recipe'
        print ' 0 - Exit'
        print '==================================================='
        response = raw_input('Enter a selection -> ')
        if response == '1': # Show all recipes
            cbk.PrintAllRecipes()
            print 'Total Recipes - %s' %cbk.totalcount
            print '--------------------------------------------------------------------------------------'
            res = raw_input('Press A Key -> ')
        elif response == '2': # Search for a recipe
            cbk.SearchForRecipe()
        elif response == '3': # Show a single recipe
            cbk.PrintAllRecipes()
            try:
                res = int(raw_input('Select a Recipe -> '))
                if res <= cbk.totalcount:
                    cbk.PrintSingleRecipe(res)
                elif res == cbk.totalcount + 1:
                    print 'Back To Menu...'
                else:
                    print 'Unrecognized command.  Returning to menu.'
            except ValueError:
                print 'Not a number...back to menu.'
        elif response == '4': # Delete Recipe
            cbk.PrintAllRecipes()
            print '0 - Return To Menu'
            try:
                res = int(raw_input('Select a Recipe to DELETE or 0 to exit -> '))
                if res != 0:
                    cbk.DeleteRecipe(res)
                elif res == '0':
                    print 'Back To Menu...'
                else:
                    print 'Unrecognized command.  Returning to menu.'
            except ValueError:
                print 'Not a number...back to menu.'
        elif response == '5': # Add a recipe
            #pass
            cbk.EnterNew()
        elif response == '6': # Print a recipe
            cbk.PrintAllRecipes()
            print '0 - Return To Menu'
            try:
                res = int(raw_input('Select a Recipe to DELETE or 0 to exit -> '))
                if res != 0:
                    cbk.PrintOut(res)
                elif res == '0':
                    print 'Back To Menu...'
                else:
                    print 'Unrecognized command.  Returning to menu.'
            except ValueError:
                print 'Not a number...back to menu.'
        elif response == '0': # Exit the program
            print 'Goodbye'
            loop = False
        else:
            print 'Unrecognized command.  Try again.'
            
Menu()
