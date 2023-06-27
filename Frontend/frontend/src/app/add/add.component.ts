import { Component } from '@angular/core';
import { ApiService } from '../api.service';
import { Model } from '../type/model';
import { FormBuilder, FormGroup, FormArray, Validators } from '@angular/forms';


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
    data: [[0],[0]],
    input: 0,
    prediction: 0
  };
  dataForm: FormGroup;
  list1: number[] = [];
  list2: number[] = [];

  constructor(private apiService: ApiService, private formBuilder: FormBuilder) { 
    this.dataForm = this.formBuilder.group({
      dataPairs: this.formBuilder.array([])
    });
  }

  ngOnInit() {
    this.addPair();
  }

  get dataPairs(): FormArray {
    return this.dataForm.get('dataPairs') as FormArray;
  }

  addPair() {
    const pair = this.formBuilder.group({
      number1: ['', Validators.required],
      number2: ['', Validators.required]
    });

    this.dataPairs.push(pair);
  }

  removePair(index: number) {
    this.dataPairs.removeAt(index);
  }

  addModel() {
    if (this.dataForm.valid) {
      this.list1 = [];
      this.list2 = [];

      const pairs = this.dataForm.value.dataPairs;

      for (const pair of pairs) {
        this.list1.push(pair.number1);
        this.list2.push(pair.number2);
      }
    } else {
      // Display error messages or take any other action if the form is not valid
    }
    console.log(this.model)
    this.model.data = [this.list1,this.list2]
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