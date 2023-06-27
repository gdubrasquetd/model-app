export interface Model {
    id?: string;
    name: string;
    nb_iterations: number;
    seed: string;
    type: string;
    data: [number[], number[]];
    input: number;
    prediction?: number;
  }
  