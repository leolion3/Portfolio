# iCal Event Generator

This simple tool can be used to generate iCal files for quick event importing into
other software like Google and Apple Calendar.

## Requirements

It requires two python modules, Flask and icalendar

```bash
pip3 install icalendar Flask
```

For using the Google Maps feature, the Google Maps API key for address autocompletion
needs to be inserted at the bottom of `templates/index.html` after the `https://maps.googleapis.com/maps/api/js?key=INSERT_HERE`.

The generated iCal file is downloaded to the client system when hitting the `Generate` button.

## Demo

![iCal Generator GUI](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/iCalGenerator/media/demo.png)