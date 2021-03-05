# Transposing, Concatenating & Joining APXS Geochemistry Data from the Mars Curiosity Rover

Mars Curiosity Rover Geochemistry!! This was a fun little night-time project inspired by a LinkedIn post from Kyle Eastman on Curiosity Rover APXS data. You can find the ioGAS file in this GitHub repo as well as the raw APXS data and the Python code I wrote to transpose and compile APSX geochemistry csv files. You'll also find the waypoints used from the Curiosity Rover to join the APXS geochemistry by sol (days on Mars). The Python code contains a docstring outling the input and output plus inline comments to walk through the methodology of the code.

There are some cool features which come out of the geochem - clearly two different primary lithology features and analyses which consist of a lot of gypsum or anhydrite as well as maybe one sample that looks like it might have some pyrite in it(?). 

The biggest challenge with this project was compiling the 921 csv geochemistry files from the Curiosity's Alpha Particle X-Ray Spectrometer (APXS). Each file contained the results of a single analysis but with a twist - the data was tipped with the element headers in rows (sigh!). Luckily I'd just learnt some introductory Python from MIT's free (yes, free! Link below!) edX course with amazing encouragement from two colleagues, James Fallon and Nejla Ghaboosi (thank you both again!). With a better idea of how Python worked and with great information from Stack Overflow (amazing!), I was able to write some code which read the csv files in and looped through each to transpose and concatenate them into one file. The code will leave the element headers from each file in deliberately so they can be checked that they’ve appended properly. Mixing elements into different columns is a pain! The error data is left in deliberately too so it can be checked. If anyone has a better way to do this and add more optionality to what is left in the final product, I’d love to get your thoughts on it! 

- GitHub link here https://github.com/TheGingaGeo/mars-curiosity-rover-apxs-geochemistry.git
- Kyle's post which inspired this project can be found here (thanks again Kyle) https://www.linkedin.com/posts/kyle-eastman-71267413a_iogas-nasa-mars-activity-6718401638689853440-64LW
-  Curiosity Rover photos and APXS data from NASA - National Aeronautics and Space Administration and JPL
- APXS data obtained through the Curiosity (MSL) Analyst's Notebook hosted by the Planetary Data System Geosciences Node at Washington University at https://an.rsl.wustl.edu/msl/
- Data imported into @imdex ioGAS, visualised and interpreted
- QGIS used for GIS visualisations and joining datasets
- Mars 15M surface geology from the USGS found here https://astrogeology.usgs.gov/search/map/Mars/Geology/Mars15MGeologicGISRenovation
- WMS of Arizona State University's 2014 release of Mars Odyssey Thermal Emission Imaging System (THEMIS) daytime infrared (IR) 100 meter/pixel mosaic (version 12) is served through this link https://planetarymaps.usgs.gov/cgi-bin/mapserv?map=/maps/mars/mars_simp_cyl.map&service=WMS&request=GetCapabilities

More information on the APXS instrument can be found here https://mars.nasa.gov/msl/spacecraft/instruments/apxs/ and info on the Curiosity Rover here https://mars.nasa.gov/msl/home/. More on the APXS data here https://an.rsl.wustl.edu/help/Content/About%20the%20data/Data%20products/MSL/APXS%20concentrations.htm?tocpath=About%20the%20data%7CData%20products%7CMSL%20(Curiosity)%7C_____1. 

MIT’s free Introduction to Computer Science and Programming Using Python edX course here:
https://www.edx.org/course/introduction-to-computer-science-and-programming-7

#Curiosity #Mars #NASA #JPL #ioGAS #QGIS #OpenData
#CuriosityStillGoingStrong 
