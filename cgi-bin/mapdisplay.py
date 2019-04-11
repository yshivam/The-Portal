#!/usr/bin/python36

print("content-type: text/html")
print("")



print("""<form action="mapsetup.py">
    <label for="fname">Name</label>
    <input type="text" id="fname" name="firstname" placeholder="John Wick">

    <label for="data">Choose the number of jobtracker you want (1-5)</label>
    <select id="data" name="data">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3">3</option>
      <option value="4">4</option>
      <option value="5">5</option>
    </select>  
    <input type="submit" value="submit">
  </form>""")
 
