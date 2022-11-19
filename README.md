## PyPiDisk

Know the amount of space a PyPi package is occupying on your hard disk.

### ? Why

You may achieve the same by using various commands on your OS. 
PyPiDisk is a just Pythonic way for the same - just in case you don't want to write commands :)

### > Install

```
pip install pypidisk
```

### ! Use

Use the command `pypidisk`

**Output**

1. In KB

<img width="300" alt="image" src="https://user-images.githubusercontent.com/76456498/202871813-a755e9d7-e372-49d3-94b9-217c89648a8c.png">


2. In MB

<img width="300" alt="image" src="https://user-images.githubusercontent.com/76456498/202871856-7448ea2f-83d9-4e44-b30f-b7df285e14c0.png">


<table>
  <tr>
     <td>Argument</td>
     <td>Help</td>
     <td>Required</td>
     <td>Default</td>
     <td>Type</td>
  </tr>
  <tr>
    <td>--size or --s</td>
    <td>Get size of package in KB or MB</td>
    <td>False</td>
    <td>KB</td>
    <td>str</td>
  </tr>
 </table>
