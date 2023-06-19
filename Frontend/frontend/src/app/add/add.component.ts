import { Component } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-ajout',
  templateUrl: './add.component.html',
  styleUrls: ['./add.component.css']
})
export class AddComponent {
  x: any;
  y: any;

  constructor(private apiService: ApiService) { }

  ajouterExemple() {
    this.apiService.ajouterExemple(this.x, this.y).subscribe(() => {
      alert('Exemple ajouté avec succès');
      this.x = '';
      this.y = '';
    });
  }
}
