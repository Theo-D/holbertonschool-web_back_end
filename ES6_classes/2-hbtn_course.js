export default class HolbertonCourse {
    constructor(name, length, students) {
      if (typeof name !== 'string') {
        throw TypeError("Name must be a string");
      }
      if (typeof length !== 'number') {
        throw TypeError("Length must be a number");
      }
      if (!Array.isArray(students)) {
        throw TypeError("Students must be an array");
      }
      for (const student of students) {
        if (typeof student !== 'string') {
          throw TypeError("Students must contain string elements");
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
      if (typeof newName !== 'string') {
        throw TypeError("Name must be a string");
      }
      this._name = newName;
    }

    // getter - setter for length.

    get length() {
      return this._length;
    }

    set length(newLength) {
      if (typeof newLength !== 'number') {
        throw TypeError("Length must be a number");
      }
      this._length = newLength;
    }

    // getter - setter for students

    get students() {
      return this._students;
    }

    set students(newStudents) {
      if (!Array.isArray(newStudents)) {
        throw TypeError("Students must be an array");
      }
      for (const elm of newStudents) {
        if (typeof elm !== 'string') {
          throw TypeError("Students must contain string elements");
        }
      }
      this._students = newStudents;
    }
  }
