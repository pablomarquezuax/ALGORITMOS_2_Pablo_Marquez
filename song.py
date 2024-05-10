from datetime import date
from genre import GENRE  # Importar la clase Genre desde el archivo genre.py

# Importar los módulos necesarios para la ejecución del programa.


class Song():
    def __init__(self, song_id, nombre, artista, duracion_segundos, fecha_lanzamiento, generos=None):
        self.song_id = song_id
        self.nombre = nombre
        self.artista = artista
        self.duracion_segundos = duracion_segundos
        self.fecha_lanzamiento = fecha_lanzamiento
        self.generos = generos

    @property
    def song_id(self):
        return self._song_id
    
    def get_id(self):
        return self._song_id
    
    
    
    def get_artist(self):
        return self._artista
    
    def get_duration(self):
        return self._duracion_segundos
    
    def get_release_date(self):
        return self._fecha_lanzamiento
    
    def get_genres(self):
        return self._generos
    
    @song_id.setter
    def song_id(self, value):
        self._song_id = value

    @property
    def nombre(self):
        return self._nombre
    
    def get_name(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser una cadena de caracteres.")
        self._nombre = value
    
    @property
    def artista(self):
        return self._artista
    
    @artista.setter
    def artista(self, value):
        if not isinstance(value, str):
            raise ValueError("El nombre del artista debe ser una cadena de caracteres.")
        self._artista = value
    
    @property
    def duracion_segundos(self):
        return self._duracion_segundos
    
    @duracion_segundos.setter
    def duracion_segundos(self, value):
        if not isinstance(value, int) or value <= 10:
            raise ValueError("La duración debe ser un número entero mayor a 10 segundos.")
        self._duracion_segundos = value
    
    @property
    def fecha_lanzamiento(self):
        return self._fecha_lanzamiento
    
    @fecha_lanzamiento.setter
    def fecha_lanzamiento(self, value):
        if not isinstance(value, date) or value > date.today():
            raise ValueError("La fecha de lanzamiento debe ser una fecha pasada.")
        self._fecha_lanzamiento = value
    
    @property
    def generos(self):
        return self._generos
    
    @generos.setter
    def generos(self, value):
        if value is None:
            self._generos = set()
        elif not isinstance(value, list):
            raise ValueError("Los géneros deben ser proporcionados como una lista de instancias de Genre.")
        elif not all(isinstance(genre, GENRE) for genre in value):
            raise ValueError("Los géneros deben ser instancias de la clase Genre.")
        elif len(value) != len(set(genre.value for genre in value)):
            raise ValueError("No puede haber géneros repetidos para la misma canción.")
        else:
            self._generos = set(value)

    def add_genre(self, genre):
        if genre not in self.generos:
            self.generos.add(genre)

    def __eq__(self, other):
        if isinstance(other, Song):
            return self._song_id == other._song_id
        return False

    def __str__(self):
        return f'{self._artista} tocando {self._nombre} durante {self._duracion_segundos} segundos.'

    """Constructor of the class.

        The constructor of the class Song is used to create a new song.

        Syntax
        ------
          song = Song(id, name, artist, duration, release_date, genres)

        Parameters
        ----------
          id : int
            The unique identifier of the song.
          name : str
            The name of the song.
          artist : str
            The artist of the song.
          duration : int
            The duration of the song in seconds.
          release_date : date
            The release date of the song.
          genres : list
            The genres of the song.

        Returns
        -------
          The new song.

        Example
        -------
          song = Song(1, "calorro", "estopa", 189, date.today(), [GENRE.POP])
        """
    #Realizar la implementación de la clase Song.






def main():
    """Function main of the module.

    The function main of this module is used to test the Class Song.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Create a Song.")
    print("=================================================================.")
    song = Song(1, "calorro", "estopa", 189, date.today(), [GENRE.POP])

    if song.get_id() == 1:
        print("Test PASS. The parameter id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_name() == "calorro":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_artist() == "estopa":
        print("Test PASS. The parameter artist has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_duration() == 189:
        print("Test PASS. The parameter duration has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_release_date() == date.today():
        print("Test PASS. The parameter release_date has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_genres() == [GENRE.POP]:
        print("Test PASS. The parameter genres has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    song2 = Song(2, "calorro", "estopa", 189, date.today(), [GENRE.POP])

    if str(song2) == "estopa tocando calorro durante 189 segundos.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
        print(str(song2))
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(song2))


    print("=================================================================.")
    print("Test Case 3: song add_genre")
    print("=================================================================.")
    song2.add_genre(GENRE.ROCK)
    genres = song2.get_genres()
    if genres == [GENRE.POP, GENRE.ROCK]:
        print("Test PASS. The method add_genre(genre) has been implemented correctly.")
    else:
        print("Test FAIL. Check the method add_genre(genre), "+ " RESULT: " + str(genres))
    
    print("=================================================================.")
    print("Test Case 4: Test the method __eq__")
    print("=================================================================.")
    song3 = Song(2, "calorro", "estopa", 189, date.today(), [GENRE.POP])
    if song2 == song3:
        print("Test PASS. The method __eq__ has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __eq__().")
    


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()