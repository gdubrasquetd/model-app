import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomePageComponent } from './home-page/home-page.component';
import { AddComponent } from './add/add.component';
import { ListingComponent } from './listing/listing.component';
import { TrainComponent } from './train/train.component';


const routes: Routes = [
  { path: '', redirectTo: 'homepage', pathMatch: 'full' },
  { path: 'homepage', component: HomePageComponent },
  { path: 'add', component: AddComponent },
  { path: 'lister', component: ListingComponent },
  { path: 'train', component: TrainComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
