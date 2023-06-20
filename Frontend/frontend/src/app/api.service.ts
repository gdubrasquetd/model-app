import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://127.0.0.1:5000'; // Remplacez par l'URL de votre API Flask

  constructor(private http: HttpClient) { }

  homepage(x: any, y: any) {
    const url = `${this.baseUrl}/`;
    const body = { x, y };
    return this.http.post(url, body);
  }

  addModel(model: string) {
    const url = `${this.baseUrl}/add`;
    const body = { model };
    return this.http.post(url, body);
  }

  getModels() {
    const url = `${this.baseUrl}/list`;
    return this.http.get(url);
  }

  effectuerInference(x: any) {
    const url = `${this.baseUrl}/inference`;
    const body = { x };
    return this.http.post(url, body);
  }

  entrainerModele() {
    const url = `${this.baseUrl}/entrainer`;
    return this.http.get(url);
  }
}
