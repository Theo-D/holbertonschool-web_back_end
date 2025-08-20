export default class HolbertonCourse {

    constructor(name, length, students) {
        if (typeof name != String) {
            throw new TypeError("Name must be a string");
        }
        if (typeof length != Number) {
            throw new TypeError("Length must be a number");
        }
        if (!Array.isArray(students)) {
            throw new TypeError("Students must be an array");
        }
        for (const student in students) {
            if (typeof student != String) {
                throw new TypeError("Students must contain string elements");
            }
        }

        this._name = name;
        this._length = length;
        this._students = students;
    }

    // getter - setter for name.
    get name() {
        return this._name;
    }

    set name(newName) {
        if (typeof newName != String) {
            throw new TypeError("Name must be a string");
        }
        this._name = newName;
    }

    // getter - setter for length.

    get length() {
        return this._length;
    }

    set length(newLength) {
        if (typeof newLength != Number) {
            throw new TypeError("Length must be a number");
        }
        this._length = newLength;
    }

    // getter - setter for students

    get students() {
        return this._students;
    }

    set students(newStudents) {
        if (!Array.isArray(newStudents)) {
            throw new TypeError("Students must be an array");
        }
        for (const elm in newStudents) {
            if (typeof elm != String) {
                throw new TypeError("Students must contain string elements");
            }
        }
        this._students = newStudents;
    }
}
