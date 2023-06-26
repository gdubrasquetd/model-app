import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Model } from './type/model'; 

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


  addModel(model: Model): Observable<any> {
    const url = `${this.baseUrl}/add`;
    return this.http.post(url, model);
  }

  deleteModel(modelId: string): Observable<any> {
    const url = `${this.baseUrl}/${modelId}`;
    return this.http.delete(url);
  }

  getModelById(modelId: string): Observable<Model> {
    const url = `${this.baseUrl}/${modelId}`;
    return this.http.get<Model>(url);
  }

  getModels() {
    const url = `${this.baseUrl}/list`;
    const modelList = this.http.get(url)
    return this.http.get(url);
  }

  trainModel(modelId: string): Observable<any> {
    const url = `${this.baseUrl}/train/${modelId}`;
    return this.http.get(url);
  }
}
