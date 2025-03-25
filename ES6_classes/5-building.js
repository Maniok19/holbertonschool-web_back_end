export default class Building {
  constructor(sqft) {
    if (this.evacuationWarningMessage() == undefined) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this.sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(val) {
    if (typeof val === 'number') this._sqft = val;
  }

  evacuationWarningMessage() {
    undefined;
  }
}
