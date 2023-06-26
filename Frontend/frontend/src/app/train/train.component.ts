import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Model } from '../type/model';

@Component({
  selector: 'app-train',
  templateUrl: './train.component.html',
  styleUrls: ['./train.component.css']
})
export class TrainComponent {
  models: Model[] = [];

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.apiService.getModels().subscribe((response: any) => {
      const models: Model[] = [];
      Object.values(response).forEach((item: any) => {
        const model: Model = {
          id: item.model.id,
          name: item.model.name,
          nb_iterations: item.model.nb_iterations,
          seed: item.model.seed,
          type: item.model.type,
          data: item.model.data,
          last_prediction: item.model.last_prediction
        };
        models.push(model);
      });
      this.models = models;
    });
  }
  deleteModelById(modelId: string): void {
    this.apiService.deleteModel(modelId).subscribe(
      response => {
        console.log((response as any).message);  
        this.apiService.getModels().subscribe(() => {
          window.location.reload();
        });
      },
      error => {
        console.log(error.error);  // Affiche l'erreur dans la console
      }
    );
  }

  trainModelById(modelId: string): void {
    this.apiService.trainModel(modelId).subscribe(
      response => {
        console.log((response as any).message);  
      },
      error => {
        console.log(error.error);  // Affiche l'erreur dans la console
      }
    );
  }
  
  
  
}
