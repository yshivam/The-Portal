#!/usr/bin/python36


print("content-type: text/html")
print("")


       
print("""

<div class="main">

        <h1>Portal's Software Services</h1>

<h3>Fill the form to use the software</h3>

<div>
  <form action="#">
    <label for="fname">Name</label>
    <input type="text" id="fname" name="firstname" placeholder="John Wick">

    <label for="software">Choose the software you want to use</label>
    <select id="soft" name="soft">
      <option value="Firefox">Mozilla Firefox</option>
      <option value="GEDIT">GEDIT Editor</option>
      <option value="VIM">VIM Editor</option>
      <option value="Sublime">Sublime Text Editor</option>
      <option value="tor">Tor Browser</option>
    </select>

    <label for="environ">Choose your desktop environment</label>
    <select id="environ" name="environ">
      <option value="Linux">Linux</option>
      <option value="Windows">Windows</option>
    </select>
  
    <input type="submit" value="Submit">
  </form>
</div>
        
    </div>
    
""")

