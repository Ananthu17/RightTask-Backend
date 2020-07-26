import { Component, OnInit } from '@angular/core'; 
import * as $ from "jquery";
import {HttpClient} from "@angular/common/http"

@Component({
  selector: 'app-attendance-page',
  templateUrl: './attendance-page.component.html',
  styleUrls: ['./attendance-page.component.css']
})
export class AttendancePageComponent implements OnInit {

  constructor(private http:HttpClient) {
    this.attendance = {}
    this.http.get('http://127.0.0.1:8000/')
    .subscribe((result)=>{
      this.attendance= result
    })

   }
  
  ngOnInit() {
    
  }

  attendance = {}

  showhide(){
    console.log("RESHMI RAJ")
    $('#rightbar').toggleClass('d-none');
    
    console.log("RESHMI RAJ")
  }
  
  onSubmit(data){
    this.http.post('http://127.0.0.1:8000/',data)
    .subscribe((result)=>{
      this.attendance= result
      console.log('data is :',this.attendance)
    })
  }

  // search
  myFunction(){
    var input: any, filter: any, table: any, tr: any, td: any, i: any, txtValue: any;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }
 
 
}
