import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://localhost:5000'; // Remplacez par l'URL de votre API Flask

  constructor(private http: HttpClient) { }

  homepage(x: any, y: any) {
    const url = `${this.baseUrl}/`;
    const body = { x, y };
    return this.http.post(url, body);
  }

  ajouterExemple(x: any, y: any) {
    const url = `${this.baseUrl}/ajouter`;
    const body = { x, y };
    return this.http.post(url, body);
  }

  listerExemples() {
    const url = `${this.baseUrl}/lister`;
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
