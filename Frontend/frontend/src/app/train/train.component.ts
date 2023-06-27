import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormArray, Validators } from '@angular/forms';

@Component({
  selector: 'app-train',
  templateUrl: './train.component.html',
  styleUrls: ['./train.component.css']
})
export class TrainComponent {
  dataForm: FormGroup;
  list1: number[] = [];
  list2: number[] = [];

  constructor(private formBuilder: FormBuilder) {
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

  onSubmit() {
    if (this.dataForm.valid) {
      this.list1 = [];
      this.list2 = [];

      const pairs = this.dataForm.value.dataPairs;

      for (const pair of pairs) {
        this.list1.push(pair.number1);
        this.list2.push(pair.number2);
      }

      console.log('List 1:', this.list1);
      console.log('List 2:', this.list2);
    } else {
      // Display error messages or take any other action if the form is not valid
    }
  }
}
