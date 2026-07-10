**\#1 ) Landing page**

**\#\# Page Title**  
**Landing Page (Welcome)**

**\#\# Page Description**  
**Purpose:**: To introduce Fishtech and allow users to explore the application. The main landing page will highlight key features such as searching for fish species, building a fish habitat and viewing an interactive map.

Mockup:  
![][image1]

\#\# Parameters Needed for the Page  
\- Query params: none  
\- Route params: none

\#\# Data Needed to Render the Page  
\- Static Content: Headline, art, feature descriptions  
\- Auth state: logged in/ not logged in for links

\#\# Link Destinations for the Page

- / main page  
- /gallery gallery of fishes  
- /build build a water system  
- /login login page  
- /signup sign up page  
- /map interactive map 

\#\# Tests for Verifying Rendering of the Page  
1\. \*\*static content render\*\*  
   \- headline, art, and features description are visible   
2\. \*\*link destination render\*\*  
   \- Each nav is present, and clicking it navigates correctly  
3\. \*\*Auth aware nav state\*\*  
   \- logged-out: /login and /signup are visible  
   \- logged-in: /login and /sign up no longer visible 

**Login page**  
Purpose: A login page that allows user to log in and unlock additional features. 

Mockup:   
\+---------------------------------------------+  
| Fishtech                    Log In          |  
|---------------------------------------------|  
| Email:    \[\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\]            |  
| Password: \[\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\]            |  
|                                             |  
|              \[ Log In \]                     |  
|---------------------------------------------|  
|             Create account                  |  
\+---------------------------------------------+

\#\# Parameters Needed for the Page

\#\# Data Needed to Render the Page  
\- UI state: email, password, validation errors, loading states  
\- API: auth endpoint response  
\- Auth state storage: token persistent and memory with auth context

\#\# Link Destinations for the Page:

- / home page  
- /signup to create an account

\#\# Tests for Verifying Rendering of the Page

1. Form element renders  
   1. Email, password, and log-in button visible  
2. Validation  
   1. Invalid input shows errors  
3. Auth success flow  
   1. Successful login store token and navigates /  
4. Auth failure flow  
   1. Shows an error message

**Fish details**  
Purpose: To search and display detailed information about fish species including habitats and water conditions.

Mockup  
![][image2]

\#\# Parameters Needed for the Page  
\- Route params: none  
\- Query params:   
	?search=fishName  
	?waterType=  
	?habitat= 

\#\# Data Needed to Render the Page  
\- UI state: search text, selected fish, search results  
\- API: Lists of fish species, information on fishes

\#\# Link Destinations for the Page

- /main page   
- /habitat builder  
- /interactive map

\#\# Tests for Verifying Rendering of the Page  
1\. \*\* search interface \*\*  
 \- Search bar and search button are visible  
2\. \*\*Display search results\*\*  
   \- Matching results to search   
3\. \*\*Fish details display\*\*  
   \- By selecting a fish, the user will view the fish name, an image of the fish, habitat information and fish information  
4\. \*\*No results\*\*  
   \- If there is not fish matching the search, a “No fish found” message will appear  
5\. \*\*Navigation\*\*  
  \- Links back to the landing page, habitat builder, log in page and interactive map 

**Habitat Builder**   
Purpose: An interactive tool that allows the user to build their own water system with fish and matches it to an existing water system if possible.

Mockup:   
![][image3]

\#\# Parameters Needed for the Page  
\- Query params:   
	?search=fishName  
	?waterType=  
	?habitat= 

\#\# Data Needed to Render the Page  
\- UI state: search text, selected fish, search results, water system parameters  
\- API: list of fish species filtered by compatibility, list of known similar water systems

\#\# Link Destinations for the Page:

- / home page

\#\# Tests for Verifying Rendering of the Page  
1\. Search renders and filter

- Search input visible, typing filters returns matching fish name

2\. Fish Selection updates state

- Selecting a fish adds it to the habitat

3\. Water system matching

- Given a combination of fish/water. An existing water system is matched by percentage

4\. Save behavior

- If logged in, the habitat data will be saved, and success is confirmed

**Interactive map**  
Purpose: To view different habitats on an interactive map. The users will be able to select a river on a map and view the different species of fishes living with and their water conditions. 

\#\# Parameters Needed for the Page  
\- Route params: none  
\- Query params:   
	?location=waterBody

\#\# Data Needed to Render the Page  
\- UI state: map view, selected location  
\- API: Lists of lakes, rivers, streams, fish species for every location, and water information for each location

\#\# Link Destinations for the Page

- /main page   
- /habitat builder  
- /fish search  
- 

\#\# Tests for Verifying Rendering of the Page  
1\. \*\* map \*\*  
 \- Interactive map is visible, limited to colorado   
2\. \*\* location selection\*\*  
   \- Clicking on a location will display information  
3\. \*\*Fish information display\*\*  
   \- A display of fish inhabiting the body of water  
4\. \*\* Habitat information display\*\*  
\- A display of habitat information  
5.\*\* No location selected \*\*  
\- If there is no valid location, a “no location found” message will appear  
6\. \*\*Navigation\*\*  
  \- Links back to the landing page, habitat builder, log in page and interactive map 

[image1]: <data:image/png;base64,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yZPuxqr2A4RtER27b775Zrm85wH81ypjt5bDsteTOyh2hy3bdjW7q+f3+eefjxdBpFXGbqNmdo8ePVrJE1+nTz75pPvnCEcldh2r5937c4SjEruOiR3sE7uOiR3sE7uOiR3sE7uOiR3sW0fs6jUodisgdrBv1bH7+uuvl19P7FZA7GDfKmP39OnT5df69NNPxW4VxA72rSp2P/744/Lr1NiK39mdO3ducePGjeXY3d394O9a5R7fVh4/fry4dOnS4vLly4s7d+6MF+/ddvHixdGS99XjlDr129TXOQqxg32rit0wdMvYffXVV4svvvhice/evVlHfdFr167tXa/dqMpRYtdUcCpuFaoKWQWwrl+/fn253jBGw/u1sJ0/f345ar1x7Gr9dp/nz5/vrVeXFy5c2Ivq3bt3l9fb/ervUdevXLmyvD5F7GDfKmLXQlcH4tiLXbtxHaMcJXY1O6vRYlcBajOu4cyu4tdUhIZq/ZoZlnrMYewqVA8ePFiOW7duvRfKuq20r9OWVfRK/b3K8D5jYgf75o5de719//3327XpydTMrv19a9lBsRver61XM7ZSsRzGrgI31O5b9zkodjWbLGIHxzNn7Opdaj12daVer1sVuxaTUrGrYFWA6q1jza7qepuxtdlWU/et9ZoKVLveItYCOVy3vs7wfvXn9nXasva1WiiHf88xsYN9c8WuHSpuZ2dneX3rYtcDsYN9c8SufjdXj1lHGGrEbg3EDvaddezevXu3fLzxY4rdGogd7DvL2LW3rlMHxxW7NRA72HdWsfv2228P7EoRuzVIi137IKht+zi1UTe5ziJ2L168WD7G8Hd0Y2K3Bomxayp47Xr75LptplObALXtIeu2uk7/Thu7ly9fLu//sccQuzVIjF1t0lMhe/jw4V7sWuTasqbWOWw7RfpymtgdNXRl42LX3nf3LO2EOy1utWdKbZvYrtfb2bZ943A7xiJ2OU4au+OErmxc7Mphy7Zdi/nUp0W9Gr6Nrbem47e1pSJYf27XxS7HSWLXTkl6nPttZOycJJuetA1ct30c9Ho9rePGbtiH46iubdxJspv6hKW38ffff4+fJp1rL8wffvjhg5+HbRntSEVzvCM5Tuzavq4fa8eUjZzZQS+ePXt25Bfypvvss89meS5HjV37YK/t63pcYgczar9b6kGb3Z21j8VuuPtXba1xUmIHMxK7jzssdu0DvRpv3rwZLz4WsYMZid3HHRS7tonWYXtFHIfYwYymYjc8OGw77uHwyNnNUV+H7ZiKw4PVHmT8NY5jVbEbftr63XffDdY8HbGDGU3Frh3lup1SoLTLOghs7UHSbmsHha3LWr/9eRjMtk1iHVC2HredoqBtsF0bb1fk6n4trhXIto9y3a+u1/Lh7WNzx64+9W2RO6vZ3JDYwYymYldqFlbhaQGr0wG00wS0wLW9Stplrds2vh6qOFUYWySHG2a3xxyGr7RY1v1qWb3m67LWr1hONWDu2LXx008/jVc5E2IHMzoodsMDHVSAKlR1WRFqQWqRq3Xrthr12hzHrqlQtfOkVBTbDK9202tnv6vHqNlbxbY95vC8Ku1yqgFnHbvxzgNn+ZZ1itjBjA6KXUVtPBOrmV7N6loE2zmO67aK0zB+Q3V7Pd7wKDFtnQpbxazFbniq0Hrsur7K2NVb1fbBQxtt+7m5iR3M6KDYze1jJ3s/iZPGrr4HLWht1J4YbW+i8QcUcxG7ULXNUv1uZNvHpltH7OZ6/Y5j1/4N6jnW9nD3799fRmwYteGoGd3U7pJix2zG/8tu+9hk64jdXIaxq7fH43+H4aiw1fq1P/DHrDJ2G3sgAOZR3/v6Qdx2NTut57LJM7xeY3eWVhk7M7sw9b0/zT6Gm0TsVkfsTkjs1kfsVucsYlefnNanseNPYZvhxsLNQeuehtidkNitj9itzlnFrozP3dE2RalNSFrs6rbaBGW4znCzk9NEUOxOSOzWR+xW56xiN5zZHRa7tvdFrdN2EWt7RpwmdEXsTkjs1kfsVuesYlfaHhLt+nAPjBa78ekpK3Zt53+xE7s4Zx274WkQaxel4U7qc0uI3aYQuxMSu/U569iNd1Nqhxqqy7ZLVAWwrrcd08+K2K2O2J2Q2K3PWceu7cBeKm4VtdrotIzfVo0/NTwtsVsdsTshsVufOWJXs7sWsopdHWljeNy14e+XzpLYrc6XX345y3MRO2YzR+zql+DD2LUjdrTNHip2FcDhW96zsOmxayeLqVBsu3oec0RJ7JjNWcfuKOY4CkfZ9NiVdgrCHsZpT3ozReyYTX3vVx27uX6m6rlseuxKRaJ+57WtY86fF7FjNuuI3Vy2JXYcTOyYjdixScSO2YgdmyQidqt4gnxI7Ngkq2rB2mL37NmzvSdZh3I2Vjd6+b7v7Owsn0ddjpcZ2zHayXdW8Z/v2mJX2gaXhmHkjlWErqw1dgCrInZABLEDIogdEEHsgAhiB0Sorq3lJNkAq2RmB0QQOyCC2AERxA6IIHZABLEDIogdEEHsgAhiB0QQOyCC2AERxA6IIHZABLEDIogdEEHsgAhiB0QQOyBCdc1h2YHumdkBEcQOiCB2QASxAyKIHRBB7IAIYgdEEDsggtgBEcQOiCB2QASxAyKIHRBB7IAIYgdEEDsggtgBEcQOiCB2QASxAyKIHRBB7IAIYgdEEDsgQnXNSbKB7pnZARHEDoggdkAEsQMiiB0QQeyACGIHRBA7IILYARHEDoggdkAEsQMiVNccCADonpkdEGEydn/88cfi33//Ha8LsLV+++23D2Nndgf0ZBy692K3u7u7DN4///wzvh/AVqh3qL/++uvizz//nI7dzz//vHfD77//voyeYRjGto3hjK5aNozd/wGT4mis4aXktwAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,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>