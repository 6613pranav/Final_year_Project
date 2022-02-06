html_code = """
<!DOCTYPE html>
<html>
<head>
</head>
<body>

<table style="text-align:center; border-collapse : collapse;" width = 900 height=500>
  <tr> 
    <td style="background:#66ffff" rowspan=3 colspan=2> <h1> Autism Test Report </h1> <i>(The generated report shouldn't be considered for medical purpose)</i></td>  
    <td style="background:#f2ccff" colspan=2> <b> Report Status </b></td>
  </tr>
  
  <tr> 
    <td  style="background:#ffffb3" colspan =2> <b style="color:#4d0066"> {0} %</b></td>
  </tr>
  
  <tr> 
    <td style="background:#ffffb3" colspan =2> &nbsp; </td>
  </tr>
  
  <tr colspan=3>&nbsp;</tr> 
  <tr colspan=3> </tr>
  <tr colspan=3> </tr>
  <tr colspan=3> </tr> 
  <tr colspan=3> </tr>
  

  <!--Patient data starts-->
  <tr><td colspan=3 style="background:#ffcce6"> <b>Patient Data </b> </td></tr>
  <tr colspan=3> </tr>
  <tr colspan=3> </tr>
  
   <tr style="background:#ffffe6"> 
    <td> Name </td>
    <td> {1}</td>
    <td colspan =2> </td>
  </tr>
  
   <tr style="background:#b3ffb3"> 
    <td> Age (in Months) </td>
    <td> {2} </td>
    <td colspan =2> </td>
  </tr>
  
  <tr style="background:#ffffe6"> 
    <td > Gender </td>
    <td> {3} </td>
    <td colspan =2></td>
  </tr>
  
  <tr style="background:#b3ffb3"> 
    <td> Test Completed By </td>
    <td> {4} </td>
    <td colspan =2> </td>
  </tr>
  
  <tr style="background:#ffffe6"> 
    <td > Email Provided </td>
    <td> {5} </td>
    <td colspan =2>  </td>
  </tr>
   
   
   <tr style="background:#b3ffb3"> 
    <td> Ethinicity </td>
    <td > {6} </td>
    <td colspan =2> </td>
  </tr>

<!--Patient data ended-->
</table>
<footer>
<p style="text-align: center;"> Thank you for using our webapp<br> Regards Audect Team</p>
</footer>

</body>
</html>"""