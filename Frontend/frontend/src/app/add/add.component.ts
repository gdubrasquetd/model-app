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
  model!: Model;

  constructor(private apiService: ApiService) { }

  addModel() {
    this.apiService.addModel(this.models).subscribe(
      response => {
        console.log((response as any).message);  // Affiche le message de succès dans la console
      },
      error => {
        console.log(error.error);  // Affiche l'erreur dans la console
      }
    );
  }

  test(){
    const modelTest: Model = {
      name: "Model 1",
      nbIterations: 100,
      seed: "12345",
      type: "local"
    };
    const modelDict: { [key: string]: any } = { ...modelTest };
    console.log(modelDict);
  }
}
