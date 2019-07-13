class Student(object):
    
    n_bed = 3
    n_bath = 2
    intrest_list = ["ML", "CS", "NLP", "Autonomus Car", "Vision"]
    area = "Morningside heights"

    
    def __init__(self, smoke, major, degree, allow_guest, 
                 budget_min, budget_max, interest, loud_music):

        self.smoke = smoke
        self.major = major
        self.degree = degree
        self.allow_guest = allow_guest
        self.budget_min = budget_min
        self.budget_max = budget_max
        self.interest = interest
        self.loud_music = loud_music
        
    def compatible(self, other):
        
        if self.allow_guest != other.allow_guest:
            return False
        
        if (self.interest or other.interest) not in self.intrest_list:
            return False
        
        if self.budget_min > other.budget_max or self.budget_max < other.budget_min:
            return False
        
        if self.loud_music + other.loud_music != 0:
            return False
        
        return True


if __name__ == '__main__':

    Jin = Student(smoke=False, major='Statistics',
                  degree='Master', allow_guest=True,
                  budget_min=1300, budget_max=1600, interest="NLP", loud_music=False)

    Colin = Student(smoke=False, major='Computer Science',
                    degree='Master', allow_guest=True,
                    budget_min=1300, budget_max=1600, interest="Autonomus Car", loud_music=False)
