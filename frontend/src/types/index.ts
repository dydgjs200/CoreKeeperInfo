// Core Keeper 게임 데이터 타입 정의

export interface Item {
  id: number;
  name: string;
  description: string;
  category: string;
  rarity: string;
  icon_url?: string;
}

export interface Recipe {
  id: number;
  result_item: Item;
  ingredients: RecipeIngredient[];
  crafting_station: string;
}

export interface RecipeIngredient {
  item: Item;
  quantity: number;
}

export interface Monster {
  id: number;
  name: string;
  hp: number;
  damage: number;
  location: string;
  drops: Drop[];
  icon_url?: string;
}

export interface Drop {
  item: Item;
  drop_rate: number;
}

export interface Boss {
  id: number;
  name: string;
  hp: number;
  damage: number;
  location: string;
  drops: Drop[];
  description: string;
  icon_url?: string;
}

export interface Biome {
  id: number;
  name: string;
  description: string;
  monsters: Monster[];
  bosses: Boss[];
}
