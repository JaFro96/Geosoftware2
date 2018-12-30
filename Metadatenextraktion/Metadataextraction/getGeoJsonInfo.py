import click, pygeoj, detailebenen, geojson

def getGeoJsonbbx(filepath, detail, folder):
    """returns the bounding Box GeoJson
    @param path Path to the file """
    points = 0
    #print("geojson")
    if detail =='bbox':
        geojson = pygeoj.load(filepath)
        geojbbx = (geojson).bbox
        #click.echo(geojbbx)
        if folder=='single':
            print("----------------------------------------------------------------")
            click.echo("Filepath:")
            click.echo(filepath)
            click.echo("Boundingbox of the GeoJSON object:")
            click.echo(geojbbx)
            print("----------------------------------------------------------------")
            return (geojbbx)
        if folder=='whole':
            detailebenen.bboxSpeicher.append(geojbbx)
            print("----------------------------------------------------------------")
            click.echo("Filepath:")
            click.echo(filepath)
            click.echo("Boundingbox of the GeoJSON object:")
            click.echo(geojbbx)
            print("----------------------------------------------------------------")
            #print(detailebenen.bboxSpeicher)
            return(geojbbx)
    if detail == 'feature':
        geojson = pygeoj.load(filepath)
        click.echo("This is a geoJSON object.")
        #TO-DO feature.geometry.coordinates in variable speichern
        for feature in geojson:
            click.echo(feature.geometry.coordinates)
    #convex_hull(points)
    return points

if __name__ == '__main__':
    getGeoJsonbbx()