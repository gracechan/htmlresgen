import grace_chan_resumes
import grace_chan_css_resumes
    
#-#######################################################################-#
#-#                                                                     #-#
#-#  remove_blanklines: str -> None                                     #-#
#-#  Purpose: removes blank lines from a file and overwrites the file   #-#
#-#                                                                     #-#
#-#######################################################################-#    

def remove_blanklines(fname):
    fin = file(fname, 'r')
    data = fin.readlines()
    fin.close

    newdata = []
    
    for line in data:
        if (line != "\n"):
            newdata += line
            
    fout = file(fname, 'w')
    fout.writelines(newdata)
    fout.close()


#-#######################################################################-#
#-#                                                                     #-#
#-#  generate_resume: str -> None                                       #-#
#-#  Purpose: generates a resume from the given file name               #-#
#-#                                                                     #-#
#-#######################################################################-#
    
def generate_resume(fname):
    fin = file(fname, 'r')
    
    # removes any blank lines found in the file
    remove_blanklines(fname)

    # get the resume format
    dataline = fin.readline().rstrip()
    datafields = dataline.split(":: ")
    fin.close()
    resumeformat = ""
    
    if (len(datafields) != 2):
        print "ERROR: Missing a field at " + datafields[0]
        return
    elif (datafields[0] != "Resume Format"):
        print "ERROR: Expected 'Resume Format', saw '" + datafields[0] + "'"
        return
    else:
        resumeformat = datafields[1]
    
    # formats the resume according to the format specified in input file
    if (resumeformat == "Copper" or resumeformat == "PD1"):
        grace_chan_resumes.create_html_resume(fname)
    elif (resumeformat == "Classic" or resumeformat == "Striped" or resumeformat == "SimplyColoured" or resumeformat == "Margarine"):
        grace_chan_css_resumes.create_html_resume(fname)
    else:
        print "ERROR: Invalid resume format chosen, saw '" + resumeformat + "'"
        return