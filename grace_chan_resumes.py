#-#######################################################################-#    
#-#                                                                     #-#
#-#  grace_chan_resumes                                                 #-#
#-#  create_html_resume: str -> None                                    #-#
#-#  Includes Classic, Copper, and PD1                                  #-#
#-#                                                                     #-#
#-#######################################################################-#    

def create_html_resume(fname):
    foutname = fname[:-4] + "-resume.html"
    
    fin = file(fname, 'r')
    fout = file(foutname, 'w')
    
    # get the resume format
    dataline = fin.readline().rstrip()
    datafields = dataline.split(":: ")
    resumeFormat = ""
    
    if (len(datafields) != 2):
        print "ERROR: Missing a field at " + datafields[0]
        return
    elif (datafields[0] != "Resume Format"):
        print "ERROR: Expected 'Resume Format', saw '" + datafields[0] + "'"
        return
    else:
        resumeFormat = datafields[1]

    # gets the name, major, id#, email, cell, phone, address
    name = ""
    major = ""
    idnum = ""
    email = ""
    cell = ""
    phone = ""
    
    if (resumeFormat == "Classic" or resumeFormat == "Copper"):
        street = ""
        city = ""
        province = ""
        postalcode = ""
        header_fields = [name, major, idnum, email, cell, phone, \
                         street, city, province, postalcode]
        header_ids = ["Name", "Term and Major", "ID #", "Email", "Cell", \
                      "Phone", "Street Name", "City", "Province", "Postal Code"]

    elif (resumeFormat == "PD1"):
        locstreet = ""
        loccity = ""
        locprovince = ""
        locpostalcode = ""
        permstreet = ""
        permcity = ""
        permprovince = ""
        permpostalcode = ""
        header_fields = [name, major, idnum, email, cell, phone, \
                         locstreet, loccity, locprovince, locpostalcode, \
                         permstreet, permcity, permprovince, permpostalcode]
        header_ids = ["Name", "Term and Major", "ID #", "Email", "Cell", \
                      "Phone", "Local Street Name", "Local City", \
                      "Local Province", "Local Postal Code", \
                      "Permanent Street Name", "Permanent City", \
                      "Permanent Province", "Permanent Postal Code"]
    
    
    for header_index in range(len(header_fields)):
        dataline = fin.readline().rstrip()
        datafields = dataline.split(":: ")
    
        if (len(datafields) != 2):
            print "ERROR: Missing a field at " + datafields[0]
            return
        elif (datafields[0] != header_ids[header_index]):
            print "ERROR: Expected '" + header_ids[header_index] + "', saw '" + datafields[0] + "'"
            return
        else:
            header_fields[header_index] = datafields[1]
    
    name = header_fields[0]
    major = header_fields[1]
    idnum = header_fields[2]
    email = header_fields[3]
    cell = header_fields[4]
    phone = header_fields[5]
    
    if (resumeFormat == "Classic" or resumeFormat == "Copper"):
        street = header_fields[6]
        city = header_fields[7]
        province = header_fields[8]
        postalcode = header_fields[9]
        address = street + ", " + city + ", " + province + ", " + postalcode
    elif (resumeFormat == "PD1"):
        locstreet = header_fields[6]
        loccity = header_fields[7]
        locprovince = header_fields[8]
        locpostalcode = header_fields[9]
        permstreet = header_fields[10]
        permcity = header_fields[11]
        permprovince = header_fields[12]
        permpostalcode = header_fields[13]
    
        
    # writes HTML for the header
    fout.write("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\"\n")
    fout.write("\"http://www.w3.org/TR/html4/loose.dtd\">\n\n")

    fout.write("<html>\n")
    fout.write("<head>\n")
    fout.write("<meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\">\n")
    fout.write("<title>" + name + "</title>\n")
    fout.write("<style type=\"text/css\">\n")
    
    if (resumeFormat=="Classic"):
        fout.write("h1 {margin-top:0px; margin-bottom:0px;}\n")
        fout.write("h1.name {position:relative; top:3px;}\n")
        fout.write("h3 {margin-top:8px; margin-bottom:0px;}\n")
        fout.write("p {margin-top:0px; margin-bottom:0px;}\n")
        fout.write("p.banner{margin-top:0px; margin-bottom:8px;}\n")
        fout.write("hr.banner {margin-top:0px; margin-bottom:0px;}\n")
        fout.write("hr {margin-top:0px;}\n")
        fout.write("ul {margin-top:0px;}\n")
        fout.write("ul.indent {margin-left:30px; margin-right:30px;}\n")
    elif (resumeFormat=="Copper"):
        fout.write("h1 {margin-top:0px; margin-bottom:0px;}\n")
        fout.write("p {margin-top:0px; margin-bottom:0px;}\n")
        fout.write("ul {margin-top:0px;}\n")
        fout.write("ul.indent {margin-left:30px; margin-right:30px;}\n")
    elif (resumeFormat=="PD1"):
        fout.write("h1 {margin-top:0px; margin-bottom:0px;}\n")
        fout.write("h3 {margin-bottom:5px;}\n")
        fout.write("p {margin-top:0px; margin-bottom:0px;}\n")
        fout.write("ul {margin-top:0px;}\n")
        fout.write("ul.indent {margin-left:30px; margin-right:30px;}\n")

    fout.write("</style>\n")
    fout.write("</head>\n\n")
    
    fout.write("<!-- " + resumeFormat + " Template created by Grace C " \
               + "generated for you by HTMLResumeGenerator v.1.0 -->\n\n")
    
    fout.write("<body>\n")
    fout.write("<table border=\"0\" align=\"center\" cellpadding=\"5\">\n")
    fout.write("<tr>\n")
    fout.write("<td>\n\n")

    #-#####################################-#
    #-#        CONTACT INFORMATION        #-#
    #-#####################################-#
    fout.write("<!-- CONTACT INFORMATION -->\n")
    
    if (resumeFormat == "Classic"):
        fout.write("<table border=\"0\" width=\"100%\" cellspacing=\"0\">\n")
        fout.write("\t<tr>\n")
        fout.write("\t\t<td align=\"center\">\n")
        fout.write("\t\t<h1>" + name.upper() + "</h1>\n")
        fout.write("\t\t<p class=\"banner\">" + major.upper() + "</p>\n")
        fout.write("\t\t<b>ID:</b> " + idnum + " &nbsp;&#8226;&nbsp; \n")
        fout.write("\t\t<b>Email:</b> " + email + " &nbsp;&#8226;&nbsp; \n")
        fout.write("\t\t<b>Cell:</b> " + cell + "<br>\n")
        if (phone != "N/A"):
            fout.write("\t\t<b>Phone:</b> " + phone + " &nbsp;&#8226;&nbsp; \n")
        fout.write("\t\t<b>Address:</b> " + address + "\n")
        fout.write("\t\t</td>\n")
        fout.write("\t</tr>\n")
        fout.write("</table>\n")
        fout.write("<br>\n\n")
    elif (resumeFormat == "Copper"):
        fout.write("<table border=\"0\" width=\"100%\" cellspacing=\"10\">\n")
        fout.write("\t<tr>\n")
        fout.write("\t\t<td width=\"40%\">\n")
        fout.write("\t\t<h1>" + name.upper() + "</h1>\n")
        fout.write("\t\t" + major.upper() + "<br>\n")
        fout.write("\t\t" + idnum + "\n")
        fout.write("\t\t</td>\n\n")
    
        fout.write("\t\t<td align=\"right\" width=\"60%\">\n")    
        if (phone != "N/A"):
            fout.write("\t\t<b>Cell:</b> " + cell + "<br>\n")
            fout.write("\t\t<b>Phone:</b> " + phone + "<br>\n")
        else:
            fout.write("\t\t" + cell + "<br>\n")    
        fout.write("\t\t" + email + "<br>\n")
        fout.write("\t\t" + address + "\n")
        fout.write("\t\t</td>\n")
        fout.write("\t</tr>\n")
        fout.write("</table>\n")
        fout.write("<hr>\n\n")
        
    elif (resumeFormat == "PD1"):
        fout.write("<table border=\"0\" width=\"100%\" cellspacing=\"0\">\n")
        fout.write("\t<tr>\n")
        fout.write("\t\t<td colspan=\"3\" align=\"center\">\n")
        fout.write("\t\t<h1>" + name + "</h1>\n")
        fout.write("\t\t" + major + "<br>\n")
        fout.write("\t\t" + idnum + "\n")
        fout.write("\t\t</td>\n\n")
        fout.write("\t</tr>\n\n")
    
        fout.write("\t<tr>\n")
        fout.write("\t\t<td width=\"30%\" align=\"center\">\n")
        fout.write("\t\t<b>Local Address:</b><br>\n")
        fout.write("\t\t" + locstreet + ",<br>\n")
        fout.write("\t\t" + loccity + ", " + locprovince + ",<br>\n")
        fout.write("\t\t" + locpostalcode + "\n")
        fout.write("\t\t</td>\n\n")
    
        fout.write("\t\t<td width=\"40%\" align=\"center\">\n")
        fout.write("\t\t<b>Email:</b> " + email + "<br>\n")    
        if (phone != "N/A"):
            fout.write("\t\t<b>Phone:</b> " + phone + "<br>\n")
        fout.write("\t\t<b>Cell:</b> " + cell + "\n")
        fout.write("\t\t</td>\n\n")
    
        fout.write("\t\t<td width=\"30%\" align=\"center\">\n")
        fout.write("\t\t<b>Permanent Address:</b><br>\n")
        fout.write("\t\t" + permstreet + ",<br>\n")
        fout.write("\t\t" + permcity + ", " + permprovince + ",<br>\n")
        fout.write("\t\t" + permpostalcode + "\n")
        fout.write("\t\t</td>\n\n")
        fout.write("\t</tr>\n")
        fout.write("</table>\n")
        fout.write("<br>\n\n")
    
    
    #-#####################################-#
    #-#           BODY OF RESUME          #-#
    #-#####################################-#
    
    #-#####################################-#
    #-#            SUBSECTIONS            #-#
    #-#####################################-#
    
    # gets the NUMBER OF SUBSECTIONS
    dataline = fin.readline().rstrip()
    datafields = dataline.split(":: ")
    numSubsections = 0
    
    if (len(datafields) != 2):
        print "ERROR: Missing a field at " + datafields[0]
        return
    elif (datafields[0] != "# of Subsections"):
        print "ERROR: Expected '# of Subsections', saw '" + datafields[0] + "'"
        return
    elif (not datafields[1].isdigit()):
        print "ERROR: Expected a number after " + datafields[0] + ", saw '" + datafields[1] + "'"
        return
    else:
        numSubsections = int(datafields[1])
    
    
    # gets the SUBSECTIONS
    for subsection_index in range(numSubsections):
        # get SUBSECTION TITLE
        dataline = fin.readline().rstrip()
        datafields = dataline.split(":: ")
        subsectionTitle = ""
        
        if (len(datafields) != 2):
            print "ERROR: Missing a field at " + datafields[0]
            return
        elif (datafields[0] != ("Subsection #" + str(subsection_index+1))):
            print "ERROR: Expected 'Subsection #" + str(subsection_index+1) \
                  + "', saw '" + datafields[0] + "'"
            return
        else:
            subsectionTitle = datafields[1]
            
        # writes HTML for subsection title to file
        fout.write("<!-- SUBSECTION #" + str(subsection_index+1) + \
                   ": " + subsectionTitle.upper() + " -->\n")
        
        if (resumeFormat == "Classic"):
            fout.write("<h3>" + subsectionTitle.upper() + "</h3>\n")
            fout.write("<hr>\n")
        elif (resumeFormat == "Copper"):
            fout.write("<hr>\n")
            fout.write("<h3>" + subsectionTitle.upper() + "</h3>\n")
        elif (resumeFormat == "PD1"):
            fout.write("<hr>\n")
            fout.write("<h3>" + subsectionTitle + "</h3>\n")
        
        fout.write("<table>\n")
        fout.write("<tr>\n")
        fout.write("<td width=\"650\">\n")
        
        
        #-#####################################-#
        #-#          SUBSECTION STYLE         #-#
        #-#####################################-#
        
        # gets SUBSECTION STYLE
        dataline = fin.readline().rstrip()
        datafields = dataline.split(":: ")
        subsectionStyle = ""
        
        if (len(datafields) != 2):
            print "ERROR: Missing a field at " + datafields[0]
            return
        elif (datafields[0] != ("Subsection Style")):
            print "ERROR: Expected 'Subsection Style', saw '" + datafields[0] + "'"
            return
        else:
            subsectionStyle = datafields[1]
            
        if (subsectionStyle == "Bullets Only"):
            
            #-#####################################-#
            #-#            BULLETS ONLY           #-#
            #-#####################################-#
            
            # gets number of bullets
            dataline = fin.readline().rstrip()
            datafields = dataline.split(":: ")
            numBullets = 0
            
            if (len(datafields) != 2):
                print "ERROR: Missing a field at " + datafields[0]
                return
            elif (datafields[0] != "# of Bullets"):
                print "ERROR: Expected '# of Bullets', saw '" + datafields[0] + "'"
                return
            elif (not datafields[1].isdigit()):
                print "ERROR: Expected a number after " + datafields[0] + ", saw '" + datafields[1] + "'"
                return
            else:
                numBullets = int(datafields[1])
                
                
            # writes HTML code for the unordered list
            fout.write("<ul>\n")            
            
            for bullet_index in range(numBullets):
                # get bullet
                dataline = fin.readline().rstrip()
                datafields = dataline.split(":: ")
                listedItem = ""
                
                if (len(datafields) != 2):
                    print "ERROR: Missing a field at " + datafields[0]
                    return
                elif (datafields[0] != ("Bullet #" + str(bullet_index+1))):
                    print "ERROR: Expected 'Bullet #" + str(bullet_index+1) \
                          + "', saw '" + datafields[0] + "'"
                    return
                else:
                    listedItem = datafields[1]

                # writes HTML code for the listed item
                fout.write("\t<li>" + listedItem + "</li>\n")
                    
            
            # writes HTML code for the end of the unordered list
            fout.write("</ul>\n")
            
        elif (subsectionStyle == "Include Positions and Dates"):            
            #-#####################################-#
            #-#    INCLUDE POSITIONS AND DATES    #-#
            #-#####################################-#
            
            # gets the NUMBER OF POSITIONS
            dataline = fin.readline().rstrip()
            datafields = dataline.split(":: ")
            numPositions = 0
            
            if (len(datafields) != 2):
                print "ERROR: Missing a field at " + datafields[0]
                return
            elif (datafields[0] != "# of Positions"):
                print "ERROR: Expected '# of Positions', saw '" + datafields[0] + "'"
                return
            elif (not datafields[1].isdigit()):
                print "ERROR: Expected a number after " + datafields[0] + ", saw '" + datafields[1] + "'"
                return
            else:
                numPositions = int(datafields[1])
                
            for position_index in range(numPositions):
                # get POSITION, LOCATION, and DATE
                position = ""
                location = ""
                date = ""
                subheader_fields = [position, location, date]
                subheader_ids = ["Position #" + str(position_index+1), \
                                 "Location", "Date"]
                
                for subheader_index in range(len(subheader_fields)):
                    dataline = fin.readline().rstrip()
                    datafields = dataline.split(":: ")
                    
                    if (len(datafields) != 2):
                        print "ERROR: Missing a field at " + datafields[0]
                        return
                    elif (datafields[0] != subheader_ids[subheader_index]):
                        print "ERROR: Expected '" \
                              + subheader_ids[subheader_index] \
                              + "', saw '" + datafields[0] + "'"
                        return
                    else:
                        subheader_fields[subheader_index] = datafields[1]

                position = subheader_fields[0]
                location = subheader_fields[1]
                date = subheader_fields[2]
            
                # writes HTML code for the position and date
                fout.write("<table border=\"0\" width=\"100%\">\n")
                fout.write("\t<tr>\n")                
                fout.write("\t\t<td width=\"75%\">\n")
                fout.write("\t\t<b>" + position + ",</b> " + location + "\n")
                fout.write("\t\t</td>\n\n")
                fout.write("\t\t<td width=\"25%\" align=\"right\">\n")
                fout.write("\t\t<i>" + date + "</i>\n")
                fout.write("\t\t</td>")
                fout.write("\t</tr>\n")
                fout.write("</table>\n")
                
                
                # gets NUMBER OF BULLETS
                dataline = fin.readline().rstrip()
                datafields = dataline.split(":: ")
                numBullets = 0
                
                if (len(datafields) != 2):
                    print "ERROR: Missing a field at " + datafields[0]
                    return
                elif (datafields[0] != "# of Bullets"):
                    print "ERROR: Expected '# of Bullets', saw '" + datafields[0] + "'"
                    return
                elif (not datafields[1].isdigit()):
                    print "ERROR: Expected a number after " + datafields[0] + ", saw '" + datafields[1] + "'"
                    return
                else:
                    numBullets = int(datafields[1])
                
                
                # writes HTML code for the unordered list
                fout.write("<ul>\n")            
            
                for bullet_index in range(numBullets):
                    # get BULLET
                    dataline = fin.readline().rstrip()
                    datafields = dataline.split(":: ")
                    listedItem = ""
                
                    if (len(datafields) != 2):
                        print "ERROR: Missing a field at " + datafields[0]
                        return
                    elif (datafields[0] != ("Bullet #" + str(bullet_index+1))):
                        print "ERROR: Expected 'Bullet #" \
                              + str(bullet_index+1) \
                              + "', saw '" + datafields[0] + "'"
                        return
                    else:
                        listedItem = datafields[1]

                        # writes HTML code for the listed item
                        fout.write("\t<li>" + listedItem + "</li>\n")
                
                # writes HTML code for the end of the unordered list
                fout.write("</ul>\n")
                
        elif (subsectionStyle == "Education"):
            #-#####################################-#
            #-#             EDUCATION             #-#
            #-#####################################-#
            
            # get the NUMBER OF INSTITUTIONS
            dataline = fin.readline().rstrip()
            datafields = dataline.split(":: ")
            numInstitutions = 0
            
            if (len(datafields) != 2):
                print "ERROR: Missing a field at " + datafields[0]
                return
            elif (datafields[0] != "# of Institutions"):
                print "ERROR: Expected '# of Institutions', saw '" \
                      + datafields[0] + "'"
                return
            elif (not datafields[1].isdigit()):
                print "ERROR: Expected a number after " + datafields[0] \
                      + ", saw '" + datafields[1] + "'"
                return
            else:
                numInstitutions = int(datafields[1])
                
            for post_index in range(numInstitutions):
                # get SCHOOL, DEGREE, PROGRAM, and DATE
                school = ""
                degree = ""
                program = ""
                date = ""
                subheader_fields = [school, degree, program, date]
                subheader_ids = ["School #" + str(post_index+1), "Degree", \
                                 "Program", "Date"]
                
                for subheader_index in range(len(subheader_fields)):
                    dataline = fin.readline().rstrip()
                    datafields = dataline.split(":: ")
                    
                    if (len(datafields) != 2):
                        print "ERROR: Missing a field at " + datafields[0]
                        return
                    elif (datafields[0] != subheader_ids[subheader_index]):
                        print "ERROR: Expected '" \
                              + subheader_ids[subheader_index] \
                              + "', saw '" + datafields[0] + "'"
                        return
                    else:
                        subheader_fields[subheader_index] = datafields[1]

                school = subheader_fields[0]
                degree = subheader_fields[1]
                program = subheader_fields[2]
                date = subheader_fields[3]
                
                # writes the HTML code for it
                fout.write("<table border=\"0\" width=\"100%\">\n")
                fout.write("\t<tr>\n")                
                fout.write("\t\t<td width=\"75%\">\n")
                
                if (program != "N/A"):
                    # post-secondary school
                    fout.write("\t\t<b>Candidate for " + degree + ",</b><br>\n")
                    fout.write("\t\t" + program + ", " + school + "\n")
                    fout.write("\t\t</td>\n\n")
                    fout.write("\t\t<td width=\"25%\" align=\"right\">\n")
                    fout.write("\t\t<i>" + date + "</i><br>\n")
                    fout.write("\t\t&#160;\n")
                else:
                    # secondary school
                    fout.write("\t\t<b>" + degree + ",</b> " \
                               + school + "\n")
                    fout.write("\t\t</td>\n\n")
                    fout.write("\t\t<td width=\"25%\" align=\"right\">\n")
                    fout.write("\t\t<i>" + date + "</i>\n")
                
                fout.write("\t\t</td>")
                fout.write("\t</tr>\n")
                fout.write("</table>\n")
                
                # gets NUMBER OF RELEVANT ASSIGNMENTS
                dataline = fin.readline().rstrip()
                datafields = dataline.split(":: ")
                numAssignments = 0
            
                if (len(datafields) != 2):
                    print "ERROR: Missing a field at " + datafields[0]
                    return
                elif (datafields[0] != "# of Relevant Assignments"):
                    print "ERROR: Expected '# of Relevant Assignments', saw '" + datafields[0] + "'"
                    return
                elif (not datafields[1].isdigit()):
                    print "ERROR: Expected a number after " + datafields[0] + ", saw '" + datafields[1] + "'"
                    return
                else:
                    numAssignments = int(datafields[1])
                    
                if (numAssignments > 0):
                    # write Relevant Assignments on the HTML resume
                    fout.write("<table border=\"0\" width=\"100%\">\n")
                    fout.write("\t<tr>\n")                
                    fout.write("\t\t<td>\n")
                    fout.write("\t\t&#160; &#160; &#160;\n")
                    fout.write("\t\t<b>Relevant Assignments:</b><br>\n")
                    fout.write("\t\t</td>\n\n")
                    fout.write("\t</tr>\n")
                    fout.write("</table>\n")
                
                for assign_index in range(numAssignments):
                    # get the ASSIGNMENT, COURSE, DATE
                    assignment = ""
                    course = ""
                    date = ""
                    relevant_fields = [assignment, course, date]
                    relevant_ids = ["Assignment #" + str(assign_index+1), \
                                    "Course", "Date"]
                    
                    for relevant_index in range(len(relevant_fields)):
                        dataline = fin.readline().rstrip()
                        datafields = dataline.split(":: ")
                        
                        if (len(datafields) != 2):
                            print "ERROR: Missing a field at " + datafields[0]
                            return
                        elif (datafields[0] != relevant_ids[relevant_index]):
                            print "ERROR: Expected '" \
                                  + relevant_ids[relevant_index] \
                                  + "', saw '" + datafields[0] + "'"
                            return
                        else:
                            relevant_fields[relevant_index] = datafields[1]
                            
                    assignment = relevant_fields[0]
                    course = relevant_fields[1]
                    date = relevant_fields[2]
                        
                    # writes the HTML code for it
                    fout.write("<table border=\"0\" width=\"100%\">\n")
                    fout.write("\t<tr>\n")                
                    fout.write("\t\t<td width=\"75%\">\n")
                    fout.write("\t\t&#160; &#160; &#160;\n")
                    fout.write("\t\t<b>" + assignment + ",</b> " \
                               + course + "\n")
                    fout.write("\t\t</td>\n\n")
                    fout.write("\t\t<td width=\"25%\" align=\"right\">\n")
                    fout.write("\t\t<i>" + date + "</i>\n")
                    fout.write("\t\t</td>")
                    fout.write("\t</tr>\n")
                    fout.write("</table>\n")
                
                    # gets NUMBER OF BULLETS
                    dataline = fin.readline().rstrip()
                    datafields = dataline.split(":: ")
                    numBullets = 0
                
                    if (len(datafields) != 2):
                        print "ERROR: Missing a field at " + datafields[0]
                        return
                    elif (datafields[0] != "# of Bullets"):
                        print "ERROR: Expected '# of Bullets', saw '" \
                              + datafields[0] + "'"
                        return
                    elif (not datafields[1].isdigit()):
                        print "ERROR: Expected a number after " \
                              + datafields[0] + ", saw '" + datafields[1] + "'"
                        return
                    else:
                        numBullets = int(datafields[1])
                
                    # writes HTML code for the unordered list
                    fout.write("<ul class=\"indent\">\n")            
            
                    for bullet_index in range(numBullets):
                        # get BULLET
                        dataline = fin.readline().rstrip()
                        datafields = dataline.split(":: ")
                        listedItem = ""
                        
                        if (len(datafields) != 2):
                            print "ERROR: Missing a field at " + datafields[0]
                            return
                        elif (datafields[0] != ("Bullet #" + str(bullet_index+1))):
                            print "ERROR: Expected 'Bullet #" \
                                  + str(bullet_index+1) \
                                  + "', saw '" + datafields[0] + "'"
                            return
                        else:
                            listedItem = datafields[1]
                            
                        # writes HTML code for the listed item
                        fout.write("\t<li>" + listedItem + "</li>\n")
                
                    # writes HTML code for the end of the unordered list
                    fout.write("</ul>\n")                    
            
        else:
            print "ERROR: Invalid subsection style chosen, '" + subsectionStyle + "'"
            return
        
        fout.write("</td>\n")
        fout.write("</tr>\n")
        fout.write("</table>\n\n\n")
    
    # ending HTML tags
    fout.write("</td></tr></table></body></html>")
        
    fin.close()
    fout.close()
    