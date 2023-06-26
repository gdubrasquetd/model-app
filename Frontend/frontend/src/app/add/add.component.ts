import { Component } from '@angular/core';
import { ApiService } from '../api.service';
import { Model } from '../type/model';

@Component({
  selector: 'app-ajout',
  templateUrl: './add.component.html',
  styleUrls: ['./add.component.css']
})
export class AddComponent {
  models!: string;
  model: Model = {
    name: '',
    nb_iterations: 0,
    seed: '',
    type: '',
    data: [0,0],
    last_prediction: 0
  };

  constructor(private apiService: ApiService) { }

  addModel() {
    console.log(this.model)
    this.apiService.addModel(this.model).subscribe(
      response => {
        console.log((response as any).message);  // Affiche le message de succès dans la console
      },
      error => {
        console.log(error.error);  // Affiche l'erreur dans la console
      }
    );
  }
}
