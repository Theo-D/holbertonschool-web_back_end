export default class Building {
    constructor (sqft) {
        // if (this.constructor == Building) {
        //     throw Error('Building is an abstract class and can\'t be instantiated');
        // }
        if ((this.constructor != Building) && (this.evacuationWarningMessage == undefined)) {
            throw Error('Class extending Building must override evacuationWarningMessage');
        }
        if (typeof sqft != 'number') {
            throw TypeError('Sqft must be a number');
        }
        this._sqft = sqft;
    }

    get sqft () {
        return this._sqft;
    }

}
