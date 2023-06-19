import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-listing',
  templateUrl: './listing.component.html',
  styleUrls: ['./listing.component.css']
})
export class ListingComponent implements OnInit {
  exemples: any[] = [];

  
  constructor(private apiService: ApiService) { }

  ngOnInit() {
    console.log("we are here")
    this.apiService.listerExemples().subscribe((response: any) => {
      this.exemples = response;
    });
  }
  entrainerModele() {
    this.apiService.entrainerModele().subscribe(() => {
      alert('Entraînement terminé');
    });
  }
  
}
