import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomePageComponent } from './home-page/home-page.component';
import { AddComponent } from './add/add.component';
import { ListingComponent } from './listing/listing.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { TrainComponent } from './train/train.component';

@NgModule({
  declarations: [
    AppComponent,
    HomePageComponent,
    AddComponent,
    ListingComponent,
    TrainComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    NgbModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
