import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Model } from '../type/model';

@Component({
  selector: 'app-listing',
  templateUrl: './listing.component.html',
  styleUrls: ['./listing.component.css']
})
export class ListingComponent implements OnInit {
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
          input: item.model.input,
          prediction: item.model.prediction
        };
        models.push(model);
      });
      this.models = models;
    });
  }
  deleteModelById(modelId: string): void {
    this.apiService.deleteModel(modelId).subscribe(
      response => {
        console.log((response as any).message);  // Affiche le message de succès dans la console
        // Mettez à jour la liste des modèles après la suppression
        this.apiService.getModels().subscribe(() => {
          window.location.reload(); // Actualise la page
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
        this.apiService.getModels().subscribe(() => {
        });
      },
      error => {
        console.log(error.error);  // Affiche l'erreur dans la console
      }
    );
  }

  predictModelById(modelId: string): void {
    this.apiService.predictModel(modelId).subscribe(
      response => {
        console.log((response as any).message);  
        this.apiService.getModels().subscribe(() => {
          window.location.reload(); // Actualise la page
        });
      },
      error => {
        console.log(error.error);  // Affiche l'erreur dans la console
      }
    );
  }
  
  
}
