class Person:

    def age(self,current_year,year_of_birth):
        return current_year - year_of_birth

    def eami_id_input(self,email_id):
        print("take email id from person and print",email_id)

    def ask_name(self):
        name = input("tel me your name")
        return name

    def ask_dob(self):
        dob = input("tell me your dob")
        return dob

s = Person()
print(s.age(2022,1992))
s.eami_id_input("jan@gamil.com")
print(s.ask_name())
print(s.ask_dob())


"""Task 1 - in a past whatever questions i have given to your with respect to list ,
tuple , dic , set , string try to create a seprate class for each and everyting and
    restructure your code for all the segment and submit .

instruction number 1 -
    always use exception handling
instrruction number 2 :
    use loggging as well

Reformat your code and submit it to me before tomorrwo's' class 3 PM IST to my mail id
sudhanshu@ineuron.ai
sunny.savita@ineuron.ai

i am only looking for your seperate python file in your github link"""