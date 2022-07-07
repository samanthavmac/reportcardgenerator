# Final GUI Report Card Generator
# Samantha Mac
# ICS2O1

# Created separate frames/variables for each
# course/skill to avoid appending when
# retrieving information

# Import modules
import tkinter
import tkinter.messagebox
import random
import library

# Define main function
def main():
    # Main window
    main_window = tkinter.Tk()
    main_window.title('Teacher Portal')
    # Main frame
    main_window_frame = tkinter.Frame(main_window)
    main_window_frame.pack(padx=40)

    # INTRO FRAME
    intro_frame = tkinter.Frame(main_window_frame)
    intro_frame.pack(anchor='w', pady=(20,0))
    # Headers
    subheader = tkinter.Label(intro_frame, \
                              text='The Samantha Ministry of Education', \
                                    font='-weight bold')
    title = tkinter.Label(intro_frame, \
                          text='Bur Oak Secondary School Teacher Portal', \
                          fg='#0e438c', font='-weight bold -size 24')
    instructions = tkinter.Label(intro_frame,\
                                 text= ('Welcome! This program will \
automatically generate a student report card based on data entered by \
you. All fields are required.'))
    # Pack labels
    subheader.pack(anchor='w')
    title.pack(anchor='w')
    instructions.pack(anchor='w')

    # TEACHER FRAME
    teacher_frame = tkinter.Frame(main_window_frame)
    teacher_frame.pack(anchor='w', pady=(30,0))
    # Label and entry
    teacher_label = tkinter.Label(teacher_frame, text='Teacher\'s Name:')
    teacher_entry = tkinter.Entry(teacher_frame, width=20)
    # Pack widgets
    teacher_label.pack(anchor='w', side='left')
    teacher_entry.pack(anchor='w', side='left')


    # DATA ENTRY SECTION

    # INFO FRAME
    info_frame = tkinter.Frame(main_window_frame)
    info_frame.pack(anchor='w', pady=(20,0))
    # Header
    info_frame_subheader = tkinter.Label\
                           (info_frame, text='Student Information', \
                            font='-weight bold -size 18')
    # Pack
    info_frame_subheader.pack(anchor='w')

    # NAME FRAME
    name_frame = tkinter.Frame(info_frame)
    name_frame.pack(anchor='w', pady=10)
    # Labels and entries
    first_name_label = tkinter.Label(name_frame, text='First Name:')
    first_name_entry = tkinter.Entry(name_frame, width=20)
    last_name_label = tkinter.Label(name_frame, text='Last Name:')
    last_name_entry = tkinter.Entry(name_frame, width=20)
    # Pack widgets
    first_name_label.pack(anchor='w', side='left')
    first_name_entry.pack(side='left')
    last_name_label.pack(side='left')
    last_name_entry.pack(side='left')

    # PRONOUN FRAME
    pronoun_frame = tkinter.Frame(info_frame)
    pronoun_frame.pack(anchor='nw', side='left', padx=(0, 25))
    # Header
    pronoun_label = tkinter.Label(pronoun_frame, text='Pronoun')
    # Pack
    pronoun_label.pack(anchor='w')

    # Radio buttons value
    pronoun_rb_value = tkinter.IntVar()
    pronoun_rb_value.set(1)
    # Radio buttons
    pronoun_rb1 = tkinter.Radiobutton\
                  (pronoun_frame, text='She', \
                   variable=pronoun_rb_value, value=1)
    pronoun_rb2 = tkinter.Radiobutton\
                  (pronoun_frame, text='He', \
                   variable=pronoun_rb_value, value=2)
    pronoun_rb3 = tkinter.Radiobutton\
                  (pronoun_frame, text='They', \
                   variable=pronoun_rb_value, value=3)
    # Pack buttons
    pronoun_rb1.pack(anchor='w')
    pronoun_rb2.pack(anchor='w')
    pronoun_rb3.pack(anchor='w')

    # GRADE FRAME
    grade_frame = tkinter.Frame(info_frame)
    grade_frame.pack(anchor='nw', side='left')
    # Header
    grade_label = tkinter.Label(grade_frame, text='Grade')
    # Pack
    grade_label.pack(anchor='w')

    # Radio buttons value
    grade_rb_value = tkinter.IntVar()
    grade_rb_value.set(4)
    # Radio buttons
    grade_rb1 = tkinter.Radiobutton\
                (grade_frame, text='9', \
                 variable=grade_rb_value, value=4)
    grade_rb2 = tkinter.Radiobutton\
                (grade_frame, text='10', \
                 variable=grade_rb_value, value=5)
    grade_rb3 = tkinter.Radiobutton\
                (grade_frame, text='11', \
                 variable=grade_rb_value, value=6)
    grade_rb4 = tkinter.Radiobutton\
                (grade_frame, text='12', \
                 variable=grade_rb_value, value=7)
    # Pack buttons
    grade_rb1.pack(anchor='w')
    grade_rb2.pack(anchor='w')
    grade_rb3.pack(anchor='w')
    grade_rb4.pack(anchor='w')

    # AVERAGE FRAME
    average_frame = tkinter.Frame(main_window_frame)
    average_frame.pack(anchor='nw', side='left', pady=(20,0))
    # Header
    average_frame_subheader = tkinter.Label\
                              (average_frame, text='Average', \
                               font='-weight bold -size 18')
    average_frame_instruction = tkinter.Label\
                                (average_frame, \
                                 text='Do not add % symbol in \
course average entry.')
    # Pack labels
    average_frame_subheader.pack(anchor='w')
    average_frame_instruction.pack(anchor='w')

    # COURSE FRAME
    course_frame = tkinter.Frame(average_frame)
    course_frame.pack()

    # COURSE 1 FRAME
    course_1_frame = tkinter.Frame(course_frame)
    course_1_frame.pack(anchor='w', pady=(10,5))
    # Labels and entries
    course_1_label = tkinter.Label\
                     (course_1_frame, text='Course 1 Name:')
    course_1_name_str = tkinter.StringVar()
    # Set entry to string var to avoid
    # scope issues when using .set() in
    # new function
    course_1_entry = tkinter.Entry(course_1_frame, textvariable=course_1_name_str, width=20)
    course_1_average_label = tkinter.Label\
                             (course_1_frame, text='Course 1 Average:')
    course_1_average_entry = tkinter.Entry(course_1_frame, width=10)
    # Pack widgets
    course_1_label.pack(anchor='w', side='left')
    course_1_entry.pack(side='left')
    course_1_average_label.pack(side='left')
    course_1_average_entry.pack(side='left')

    # COURSE 2 FRAME
    course_2_frame = tkinter.Frame(course_frame)
    course_2_frame.pack(anchor='w', pady=(0,5))
    # Labels and entries
    course_2_label = tkinter.Label\
                     (course_2_frame, text='Course 2 Name:')
    course_2_name_str = tkinter.StringVar()
    course_2_entry = tkinter.Entry(course_2_frame, textvariable=course_2_name_str, width=20)
    course_2_average_label = tkinter.Label\
                             (course_2_frame, text='Course 2 Average:')
    course_2_average_entry = tkinter.Entry(course_2_frame, width=10)
    # Pack widgets
    course_2_label.pack(anchor='w', side='left')
    course_2_entry.pack(side='left')
    course_2_average_label.pack(side='left')
    course_2_average_entry.pack(side='left')

    # COURSE 3 FRAME
    course_3_frame = tkinter.Frame(course_frame)
    course_3_frame.pack(anchor='w', pady=(0,5))
    # Labels and entries
    course_3_label = tkinter.Label\
                     (course_3_frame, text='Course 3 Name:')
    course_3_name_str = tkinter.StringVar()
    course_3_entry = tkinter.Entry(course_3_frame, textvariable=course_3_name_str, width=20)
    course_3_average_label = tkinter.Label\
                             (course_3_frame, text='Course 3 Average:')
    course_3_average_entry = tkinter.Entry(course_3_frame, width=10)
    # Pack widgets
    course_3_label.pack(anchor='w', side='left')
    course_3_entry.pack(side='left')
    course_3_average_label.pack(side='left')
    course_3_average_entry.pack(side='left')

    # COURSE 4 FRAME
    course_4_frame = tkinter.Frame(course_frame)
    course_4_frame.pack(anchor='w', side='left', pady=(0,5))
    # Labels and entries
    course_4_label = tkinter.Label\
                     (course_4_frame, text='Course 4 Name:')
    course_4_name_str = tkinter.StringVar()
    course_4_entry = tkinter.Entry(course_4_frame, textvariable=course_4_name_str, width=20)
    course_4_average_label = tkinter.Label\
                             (course_4_frame, text='Course 4 Average:')
    course_4_average_entry = tkinter.Entry(course_4_frame, width=10)
    # Pack widgets
    course_4_label.pack(anchor='w', side='left')
    course_4_entry.pack(side='left')
    course_4_average_label.pack(side='left')
    course_4_average_entry.pack(side='left')


    # SKILLS FRAME
    skills_frame = tkinter.Frame(main_window_frame)
    skills_frame.pack(anchor='nw', pady=(20,0), padx=(50, 0))
    # Headers
    skills_frame_subheader = tkinter.Label\
                             (skills_frame, \
                              text='Learning Skills', \
                              font='-weight bold -size 18')
    skills_frame_subheader.pack(anchor='w')

    # ROW 1 FRAME
    row_1_frame = tkinter.Frame(skills_frame)
    row_1_frame.pack(anchor='w', pady=5)
    # ROW 2 FRAME
    row_2_frame = tkinter.Frame(skills_frame)
    row_2_frame.pack(anchor='w', pady=5)

    # RESPONSIBILITY FRAME
    responsibility_frame = tkinter.Frame(row_1_frame, width=60)
    responsibility_frame.pack(anchor='nw', side='left', padx=(0,30))
    # Header
    responsibility_label = tkinter.Label\
                           (responsibility_frame, text='Responsibility')
    # Pack
    responsibility_label.pack(anchor='w')
    
    # Radio buttons value
    responsibility_rb_value = tkinter.IntVar()
    responsibility_rb_value.set(8)
    # Radio buttons
    responsibility_rb1 = tkinter.Radiobutton\
                         (responsibility_frame, text='E', \
                          variable=responsibility_rb_value, value=8)
    responsibility_rb2 = tkinter.Radiobutton\
                         (responsibility_frame, text='G', \
                          variable=responsibility_rb_value, value=9)
    responsibility_rb3 = tkinter.Radiobutton\
                         (responsibility_frame, text='S', \
                          variable=responsibility_rb_value, value=10)
    responsibility_rb4 = tkinter.Radiobutton\
                         (responsibility_frame, text='N', \
                          variable=responsibility_rb_value, value=11)
    # Pack buttons
    responsibility_rb1.pack(anchor='w')
    responsibility_rb2.pack(anchor='w')
    responsibility_rb3.pack(anchor='w')
    responsibility_rb4.pack(anchor='w')

    # ORGANIZATION FRAME
    organization_frame = tkinter.Frame(row_1_frame)
    organization_frame.pack(anchor='nw', side='left', padx=(0,30))
    # Header
    organization_label = tkinter.Label\
                         (organization_frame, text='Organization')
    # Pack
    organization_label.pack(anchor='w')
    
    # Radio buttons value
    organization_rb_value = tkinter.IntVar()
    organization_rb_value.set(8)
    # Radio buttons
    organization_rb1 = tkinter.Radiobutton(organization_frame, text='E', variable=organization_rb_value, value=8)
    organization_rb2 = tkinter.Radiobutton(organization_frame, text='G', variable=organization_rb_value, value=9)
    organization_rb3 = tkinter.Radiobutton(organization_frame, text='S', variable=organization_rb_value, value=10)
    organization_rb4 = tkinter.Radiobutton(organization_frame, text='N', variable=organization_rb_value, value=11)
    # Pack buttonsresponsibility_rb1.pack(anchor='w')
    organization_rb1.pack(anchor='w')
    organization_rb2.pack(anchor='w')
    organization_rb3.pack(anchor='w')
    organization_rb4.pack(anchor='w')

    # INDEPENDENT WORK FRAME
    independent_work_frame = tkinter.Frame(row_1_frame)
    independent_work_frame.pack(anchor='nw', side='left', padx=(0,30))
    # Header
    independent_work_label = tkinter.Label(independent_work_frame, text='Independent Work')
    # Pack
    independent_work_label.pack(anchor='w')
    
    # Radio buttons value
    independent_work_rb_value = tkinter.IntVar()
    independent_work_rb_value.set(8)
    # Radio buttons
    independent_work_rb1 = tkinter.Radiobutton(independent_work_frame, text='E', variable=independent_work_rb_value, value=8)
    independent_work_rb2 = tkinter.Radiobutton(independent_work_frame, text='G', variable=independent_work_rb_value, value=9)
    independent_work_rb3 = tkinter.Radiobutton(independent_work_frame, text='S', variable=independent_work_rb_value, value=10)
    independent_work_rb4 = tkinter.Radiobutton(independent_work_frame, text='N', variable=independent_work_rb_value, value=11)
    # Pack buttons
    independent_work_rb1.pack(anchor='w')
    independent_work_rb2.pack(anchor='w')
    independent_work_rb3.pack(anchor='w')
    independent_work_rb4.pack(anchor='w')

    # COLLABORATION FRAME
    collaboration_frame = tkinter.Frame(row_2_frame)
    collaboration_frame.pack(anchor='nw', side='left', padx=(0,30))
    # Header
    collaboration_label = tkinter.Label(collaboration_frame, text='Collaboration')
    # Pack
    collaboration_label.pack(anchor='w')
    
    # Radio buttons value
    collaboration_rb_value = tkinter.IntVar()
    collaboration_rb_value.set(8)
    # Radio buttons
    collaboration_rb1 = tkinter.Radiobutton(collaboration_frame, text='E', variable=collaboration_rb_value, value=8)
    collaboration_rb2 = tkinter.Radiobutton(collaboration_frame, text='G', variable=collaboration_rb_value, value=9)
    collaboration_rb3 = tkinter.Radiobutton(collaboration_frame, text='S', variable=collaboration_rb_value, value=10)
    collaboration_rb4 = tkinter.Radiobutton(collaboration_frame, text='N', variable=collaboration_rb_value, value=11)
    # Pack buttons
    collaboration_rb1.pack(anchor='w')
    collaboration_rb2.pack(anchor='w')
    collaboration_rb3.pack(anchor='w')
    collaboration_rb4.pack(anchor='w')

    # INITIATIVE FRAME
    initiative_frame = tkinter.Frame(row_2_frame)
    initiative_frame.pack(anchor='nw', side='left', padx=(0,60))
    # Header
    initiative_label = tkinter.Label(initiative_frame, text='Initiative')
    # Pack
    initiative_label.pack(anchor='w')
    
    # Radio buttons value
    initiative_rb_value = tkinter.IntVar()
    initiative_rb_value.set(8)
    # Radio buttons
    initiative_rb1 = tkinter.Radiobutton(initiative_frame, text='E', variable=initiative_rb_value, value=8)
    initiative_rb2 = tkinter.Radiobutton(initiative_frame, text='G', variable=initiative_rb_value, value=9)
    initiative_rb3 = tkinter.Radiobutton(initiative_frame, text='S', variable=initiative_rb_value, value=10)
    initiative_rb4 = tkinter.Radiobutton(initiative_frame, text='N', variable=initiative_rb_value, value=1)
    # Pack buttons
    initiative_rb1.pack(anchor='w')
    initiative_rb2.pack(anchor='w')
    initiative_rb3.pack(anchor='w')
    initiative_rb4.pack(anchor='w')

    # SELF REGULATION FRAME
    self_regulation_frame = tkinter.Frame(row_2_frame)
    self_regulation_frame.pack(anchor='nw', side='left', padx=(0,30))
    # Header
    self_regulation_label = tkinter.Label(self_regulation_frame, text='Self Regulation')
    # Pack
    self_regulation_label.pack(anchor='w')
    
    # Radio buttons value
    self_regulation_rb_value = tkinter.IntVar()
    self_regulation_rb_value.set(8)
    # Radio buttons
    self_regulation_rb1 = tkinter.Radiobutton(self_regulation_frame, text='E', variable=self_regulation_rb_value, value=8)
    self_regulation_rb2 = tkinter.Radiobutton(self_regulation_frame, text='G', variable=self_regulation_rb_value, value=9)
    self_regulation_rb3 = tkinter.Radiobutton(self_regulation_frame, text='S', variable=self_regulation_rb_value, value=10)
    self_regulation_rb4 = tkinter.Radiobutton(self_regulation_frame, text='N', variable=self_regulation_rb_value, value=11)
    # Pack buttons
    self_regulation_rb1.pack(anchor='w')
    self_regulation_rb2.pack(anchor='w')
    self_regulation_rb3.pack(anchor='w')
    self_regulation_rb4.pack(anchor='w')

    # BUTTON COMMAND TO CREATE NEW WINDOW
    def generate_report():
        # ENTRY DATA RETRIEVALS
        # Teacher var
        teacher = teacher_entry.get()
        # Name var
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        # Course name var
        course_1_name = course_1_name_str.get()
        course_2_name = course_2_name_str.get()
        course_3_name = course_3_name_str.get()
        course_4_name = course_4_name_str.get()
        # Average var
        course_1_average = float(course_1_average_entry.get())
        course_2_average = float(course_2_average_entry.get())
        course_3_average = float(course_3_average_entry.get())
        course_4_average = float(course_4_average_entry.get())
        # Calculate final average by importing
        # function from module
        # Pass var from this file as args
        final_average = library.calculate_average(course_1_average, course_2_average, course_3_average, course_4_average)
        

        # RADIO BUTTON DATA RETRIEVALS
        # BASIC INFO
        # Pronoun
        pronoun_get = pronoun_rb_value.get()
        # Use pronoun function converter from module
        possessive_pronoun = library.select_possessive_pronoun(pronoun_get)
        verb_pronoun = library.select_verb_pronoun(pronoun_get)
        # Grade
        grade_get = grade_rb_value.get()
        grade = library.select_grade(grade_get)

        # LEARNING SKILLS
        # Responsibility
        responsibility_get = responsibility_rb_value.get()
        responsibility_rating = library.select_responsibility_rating(responsibility_get)
        # Organization
        organization_get = organization_rb_value.get()
        organization_rating = library.select_organization_rating(organization_get)
        # Independent work
        independent_work_get = independent_work_rb_value.get()
        independent_work_rating = library.select_independent_work_rating(independent_work_get)
        # Collaboration
        collaboration_get = collaboration_rb_value.get()
        collaboration_rating = library.select_collaboration_rating(collaboration_get)
        # Initiative
        initiative_get = initiative_rb_value.get()
        initiative_rating = library.select_initiative_rating(initiative_get)
        # Self Regulation
        self_regulation_get = self_regulation_rb_value.get()
        self_regulation_rating = library.select_self_regulation_rating(self_regulation_get)

            
        # CARD WINDOW
        # New window
        card_window = tkinter.Tk()
        card_window.title(first_name + ' ' + last_name + '\'s Report Card')
        # Main frame
        card_window_frame = tkinter.Frame(card_window)
        card_window_frame.pack(anchor='w',padx=40)

        # INTRO FRAME
        output_header_frame = tkinter.Frame(card_window_frame)
        output_header_frame.pack(anchor='w', pady=(20,0))
        # Header
        output_subheader = tkinter.Label(output_header_frame, text='The Samantha Ministry of Education', font='-weight bold')
        output_title = tkinter.Label(output_header_frame, text=('Student Report Card'), fg='#0e438c', font='-weight bold -size 24')
        # Pack labels
        output_subheader.pack(anchor='w')
        output_title.pack(anchor='w')

        # INFO FRAME
        # Create rows to organize labels
        # and their relational positioning
        output_info_frame = tkinter.Frame(card_window_frame)
        output_row_1 = tkinter.Frame(output_info_frame)
        output_row_2 = tkinter.Frame(output_info_frame)
        output_row_3 = tkinter.Frame(output_info_frame)
        output_row_4 = tkinter.Frame(output_info_frame)
        # Pack frames
        output_info_frame.pack(anchor='w', pady=(20,0))
        output_row_1.pack(anchor='w')
        output_row_2.pack(anchor='w')
        output_row_3.pack(anchor='w')
        output_row_4.pack(anchor='w')


        # Student name
        # Add standard height and width to label
        # Add border (relief=style of border)
        # Concatenate text using data
        # retrieved from entries
        output_student_label = tkinter.Label(output_row_1, \
                                             text=('Student: ' + first_name + ' ' + last_name), \
                                             anchor='w', height=2, width=40, padx=10, \
                                             borderwidth=0.5, relief='solid')
        # OEN
        OEN = library.randomize_OEN()
        output_OEN_label = tkinter.Label(output_row_1, \
                                             text=('OEN: ' + OEN), \
                                             anchor='w', height=2, width=20, padx=10, \
                                             borderwidth=0.5, relief='solid')
        # Grade
        output_grade_label = tkinter.Label(output_row_2, text=('Grade: ' + grade), \
                                             anchor='w', height=2, width=20, padx=10, \
                                             borderwidth=0.5, relief='solid')
        # Teacher
        output_teacher_label = tkinter.Label(output_row_2, text=('Teacher: ' + teacher), \
                                             anchor='w', height=2, width=40, padx=10, \
                                             borderwidth=0.5, relief='solid')
        # School
        school_label = tkinter.Label(output_row_3, text=('School: Bur Oak Secondary School'), \
                                             anchor='w', height=2, width=62, padx=10, \
                                             borderwidth=0.5, relief='solid')
        # Address
        address_label = tkinter.Label(output_row_4, text=('Address: 933 Bur Oak Ave, Markham, ON L6E 1G4'), \
                                             anchor='w', height=2, width=40, padx=10, \
                                             borderwidth=0.5, relief='solid')
        # Teacher
        principal_label = tkinter.Label(output_row_4, text=('Principal: Ms. Rose Li'), \
                                             anchor='w', height=2, width=20, padx=10, \
                                             borderwidth=0.5, relief='solid')
        # Pack labels
        output_student_label.pack(anchor='w', side='left')
        output_OEN_label.pack(anchor='w', side='left')
        output_grade_label.pack(anchor='w', side='left')
        output_teacher_label.pack(anchor='w', side='left')
        school_label.pack(anchor='w')
        address_label.pack(anchor='w', side='left')
        principal_label.pack(anchor='w', side='left')


        # DATA FRAME
        output_data_frame = tkinter.Frame(card_window_frame)
        output_data_frame.pack(anchor='w', pady=(30,0))
        
        # AVERAGE FRAME
        output_average_frame = tkinter.Frame(output_data_frame)
        output_average_frame.pack(anchor='nw', side='left')
        # Header
        output_average_frame_subheader = tkinter.Label(output_average_frame, text='Average', font='-weight bold -size 18')
        output_average_frame_subheader.pack(anchor='w', pady=(0,10))
        # Table rows
        output_row_5 = tkinter.Frame(output_average_frame)
        output_row_6 = tkinter.Frame(output_average_frame)
        output_row_7 = tkinter.Frame(output_average_frame)
        output_row_8 = tkinter.Frame(output_average_frame)
        output_row_9 = tkinter.Frame(output_average_frame)
        # Pack frames
        output_row_5.pack(anchor='w')
        output_row_6.pack(anchor='w')
        output_row_7.pack(anchor='w')
        output_row_8.pack(anchor='w')
        output_row_9.pack(anchor='w')

        # Final Average
        output_final_label = tkinter.Label(output_row_5, text=('Final Average'), font='-weight bold', \
                                             anchor='w', height=2, width=25, padx=10, \
                                             borderwidth=0.5, relief='solid')
        output_final_average_label = tkinter.Label(output_row_5, text=(str(final_average) + '%'), font='-weight bold', \
                                             anchor='e', height=2, width=8, padx=10, \
                                             borderwidth=0.5, relief='solid')
        # Course 1
        output_course_1_label = tkinter.Label(output_row_6, text=(course_1_name), \
                                             anchor='w', height=2, width=25, padx=10, \
                                             borderwidth=0.5, relief='solid')
        output_course_1_average_label = tkinter.Label(output_row_6, text=(str(course_1_average) + '%'), \
                                             anchor='e', height=2, width=8, padx=10, \
                                             borderwidth=0.5, relief='solid')
        # Course 2
        output_course_2_label = tkinter.Label(output_row_7, text=(course_2_name), \
                                             anchor='w', height=2, width=25, padx=10, \
                                             borderwidth=0.5, relief='solid')
        output_course_2_average_label = tkinter.Label(output_row_7, text=(str(course_2_average) + '%'), \
                                             anchor='e', height=2, width=8, padx=10, \
                                             borderwidth=0.5, relief='solid')
        # Course 3
        output_course_3_label = tkinter.Label(output_row_8, text=(course_3_name), \
                                             anchor='w', height=2, width=25, padx=10, \
                                             borderwidth=0.5, relief='solid')
        output_course_3_average_label = tkinter.Label(output_row_8, text=(str(course_3_average) + '%'), \
                                             anchor='e', height=2, width=8, padx=10, \
                                             borderwidth=0.5, relief='solid')
        # Course 4
        output_course_4_label = tkinter.Label(output_row_9, text=(course_4_name), \
                                             anchor='w', height=2, width=25, padx=10, \
                                             borderwidth=0.5, relief='solid')
        output_course_4_average_label = tkinter.Label(output_row_9, text=(str(course_4_average) + '%'), \
                                             anchor='e', height=2, width=8, padx=10, \
                                             borderwidth=0.5, relief='solid')

        # Pack widgets
        output_final_label.pack(anchor='w', side='left')
        output_final_average_label.pack(anchor='w', side='left')
        output_course_1_label.pack(anchor='w', side='left')
        output_course_1_average_label.pack(anchor='w', side='left')
        output_course_2_label.pack(anchor='w', side='left')
        output_course_2_average_label.pack(anchor='w', side='left')
        output_course_3_label.pack(anchor='w', side='left')
        output_course_3_average_label.pack(anchor='w', side='left')
        output_course_4_label.pack(anchor='w', side='left')
        output_course_4_average_label.pack(anchor='w', side='left')
        


        # SKILLS FRAME
        output_skills_frame = tkinter.Frame(output_data_frame)
        output_skills_frame.pack(anchor='w', padx=(50,0))
        # Header
        output_skills_frame_subheader = tkinter.Label(output_skills_frame, text='Learning Skills', font='-weight bold -size 18')
        output_skills_frame_subheader.pack(anchor='nw', pady=(0,10))
        # Table rows
        output_row_10 = tkinter.Frame(output_skills_frame)
        output_row_11 = tkinter.Frame(output_skills_frame)
        output_row_12 = tkinter.Frame(output_skills_frame)
        output_row_13 = tkinter.Frame(output_skills_frame)
        output_row_14 = tkinter.Frame(output_skills_frame)
        output_row_15 = tkinter.Frame(output_skills_frame)
        # Pack frames
        output_row_10.pack(anchor='w')
        output_row_11.pack(anchor='w')
        output_row_12.pack(anchor='w')
        output_row_13.pack(anchor='w')
        output_row_14.pack(anchor='w')
        output_row_15.pack(anchor='w')

        # Responsibility
        output_responsibility_label = tkinter.Label(output_row_10, text=('Responsibility'), \
                                             anchor='w', height=2, width=15, padx=10, \
                                             borderwidth=0.5, relief='solid')
        output_responsibility_rating_label = tkinter.Label(output_row_10, text=(responsibility_rating), \
                                             anchor='e', height=2, width=2, padx=10, \
                                             borderwidth=0.5, relief='solid')
        # Organiation
        output_organization_label = tkinter.Label(output_row_11, text=('Organization'), \
                                             anchor='w', height=2, width=15, padx=10, \
                                             borderwidth=0.5, relief='solid')
        output_organization_rating_label = tkinter.Label(output_row_11, text=(organization_rating), \
                                             anchor='e', height=2, width=2, padx=10, \
                                             borderwidth=0.5, relief='solid')
        # Independent Work
        output_independent_work_label = tkinter.Label(output_row_12, text=('Independent Work'), \
                                             anchor='w', height=2, width=15, padx=10, \
                                             borderwidth=0.5, relief='solid')
        output_independent_work_rating_label = tkinter.Label(output_row_12, text=(independent_work_rating), \
                                             anchor='e', height=2, width=2, padx=10, \
                                             borderwidth=0.5, relief='solid')
        # Collaboration
        output_collaboration_label = tkinter.Label(output_row_13, text=('Collaboration'), \
                                             anchor='w', height=2, width=15, padx=10, \
                                             borderwidth=0.5, relief='solid')
        output_collaboration_rating_label = tkinter.Label(output_row_13, text=(collaboration_rating), \
                                             anchor='e', height=2, width=2, padx=10, \
                                             borderwidth=0.5, relief='solid')
        # Initiative
        output_initiative_label = tkinter.Label(output_row_14, text=('Initiative'), \
                                             anchor='w', height=2, width=15, padx=10, \
                                             borderwidth=0.5, relief='solid')
        output_initiative_rating_label = tkinter.Label(output_row_14, text=(initiative_rating), \
                                             anchor='e', height=2, width=2, padx=10, \
                                             borderwidth=0.5, relief='solid')
        # Self Regulation
        output_self_regulation_label = tkinter.Label(output_row_15, text=('Self-Regulation'), \
                                             anchor='w', height=2, width=15, padx=10, \
                                             borderwidth=0.5, relief='solid')
        output_self_regulation_rating_label = tkinter.Label(output_row_15, text=(self_regulation_rating), \
                                             anchor='e', height=2, width=2, padx=10, \
                                             borderwidth=0.5, relief='solid')
        # Pack labels
        output_responsibility_label.pack(anchor='w', side='left')
        output_responsibility_rating_label.pack(anchor='w')
        output_organization_label.pack(anchor='w', side='left')
        output_organization_rating_label.pack(anchor='w')
        output_independent_work_label.pack(anchor='w', side='left')
        output_independent_work_rating_label.pack(anchor='w')
        output_collaboration_label.pack(anchor='w', side='left')
        output_collaboration_rating_label.pack(anchor='w')
        output_initiative_label.pack(anchor='w', side='left')
        output_initiative_rating_label.pack(anchor='w')
        output_self_regulation_label.pack(anchor='w', side='left')
        output_self_regulation_rating_label.pack(anchor='w')


        # FINAL COMMENT
        output_comment_frame = tkinter.Frame(card_window)
        output_comment_frame.pack(anchor='w', pady=(30,0), padx=40)
        # Header
        output_comment_subheader = tkinter.Label(output_comment_frame, text='Teacher\'s Comment', font='-weight bold -size 18')
        output_comment_subheader.pack(anchor='w')

        # Retrieve statements
        average_statement = library.select_average_statement(final_average, first_name)
        responsibility_statement = library.select_responsibility_statement(responsibility_rating, possessive_pronoun, verb_pronoun)
        organization_statement = library.select_organization_statement(organization_rating, possessive_pronoun, verb_pronoun)
        independent_work_statement = library.select_independent_work_statement(independent_work_rating, possessive_pronoun, verb_pronoun)
        collaboration_statement = library.select_collaboration_statement(collaboration_rating, possessive_pronoun, verb_pronoun)
        initiative_statement = library.select_initiative_statement(initiative_rating, possessive_pronoun, verb_pronoun)
        self_regulation_statement = library.select_self_regulation_statement(self_regulation_rating, possessive_pronoun, verb_pronoun)
        skill_statement_1, skill_statement_2, skill_statement_3 = library.select_skill(responsibility_statement, organization_statement, \
                 independent_work_statement, collaboration_statement, \
                 initiative_statement, self_regulation_statement)
        

        # Body
        output_comment_label = tkinter.Label(output_comment_frame, \
                                             text=(average_statement + '\n' + skill_statement_1 + '\n' + skill_statement_2 + '\n' + skill_statement_3),\
                                             anchor='w', justify='left')
        # Pack widgets
        output_comment_label.pack(anchor='w', pady=(5,0))

        # Reset fields for next student
        teacher_entry.delete(0, tkinter.END)
        first_name_entry.delete(0, tkinter.END)
        last_name_entry.delete(0, tkinter.END)
        pronoun_rb_value.set(1)
        grade_rb_value.set(4)
        course_1_entry.delete(0, tkinter.END)
        course_2_entry.delete(0, tkinter.END)
        course_3_entry.delete(0, tkinter.END)
        course_4_entry.delete(0, tkinter.END)
        course_1_average_entry.delete(0, tkinter.END)
        course_2_average_entry.delete(0, tkinter.END)
        course_3_average_entry.delete(0, tkinter.END)
        course_4_average_entry.delete(0, tkinter.END)
        responsibility_rb_value.set(8)
        organization_rb_value.set(8)
        independent_work_rb_value.set(8)
        collaboration_rb_value.set(8)
        initiative_rb_value.set(8)
        self_regulation_rb_value.set(8)


        # BUTTON FRAME
        output_button_frame = tkinter.Frame(card_window)
        output_button_frame.pack(anchor='w', pady=(20,30), padx=40)

        # Quit button
        output_quit_button = tkinter.Button(output_button_frame, text='Quit', command=card_window.destroy)
        # Pack
        output_quit_button.pack(anchor='w')


        # INPUT VALIDATIONS
        # Use if to test ALL conditions
        if teacher == '':
            tkinter.messagebox.showinfo('Teacher Error', 'ERROR! \'Teacher\'s Name\' field required.')
            card_window.destroy()
        if first_name == '' or last_name == '':
            tkinter.messagebox.showinfo('Name Error', 'ERROR! \'First Name\' and \'Last Name\' field required.')
            card_window.destroy()
        # Only play if first two conditions are not met
        # to prevent overload of errors
        if course_1_name == '' or course_2_name == '' or course_3_name == '' or course_4_name == '':
            tkinter.messagebox.showinfo('Course Name Error', 'ERROR! \'Course Name\' field(s) required.')
            card_window.destroy()
        if (course_1_average < 0 or course_1_average > 100 or \
             course_2_average < 0 or course_2_average > 100 or \
             course_3_average < 0 or course_3_average > 100 or \
             course_4_average < 0 or course_4_average > 100):
            tkinter.messagebox.showinfo('Course Average Error', \
                                        'ERROR! Course average must be greater than or equal to 0 or less than or equal to 100.')
            card_window.destroy()
        


        
    # BUTTON FRAME
    # Must be placed after func
    main_button_frame = tkinter.Frame(main_window)
    main_button_frame.pack(anchor='w', pady=(20,30), padx=40)
    # Buttons
    generate_button = tkinter.Button(main_button_frame, text='Generate', command=generate_report)
    quit_button = tkinter.Button(main_button_frame, text='Quit', command=main_window.destroy)
    # Pack buttons
    generate_button.pack(side='left')
    quit_button.pack(side='left')

    # Main loop
    tkinter.mainloop()

# Call on main function
main()
