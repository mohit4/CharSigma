from django.db import models

# Create your models here.
class Character(models.Model):
    """
    Defines all the traits of a character ranging from physical attributes to
    special abilites and nature of the character
    """

    SKIN_COLOR_CHOICES = (
        ('#800000', 'Maroon'), ('#8B0000', 'DarkRed'), ('#B22222', 'Fire Brick'), ('#FF0000', 'Red'),
        ('#FA8072', 'Salmon'), ('#FF6347', 'Tomato'), ('#FF7F50', 'Coral'), ('#FF4500', 'OrangeRed'),
        ('#D2691E', 'Chocolate'), ('#F4A460', 'Sandy Brown'), ('#FF8C00', 'Dark Orange'), ('#FFA500', 'Orange'),
        ('#B8860B', 'DarkGoldenrod'), ('#DAA520', 'Goldenrod'), ('#FFD700', 'Gold'), ('#808000', 'Olive'),
        ('#FFFF00', 'Yellow'), ('#9ACD32', 'Yellow Green'), ('#ADFF2F', 'Green Yellow'), ('#7FFF00', 'Chartreuse'),
        ('#7CFC00', 'Lawn Green'), ('#008000', 'Green'), ('#00FF00', 'Lime'), ('#32CD32', 'Lime Green'),
        ('#00FF7F', 'Spring Green'), ('#00FA9A', 'Medium Spring Green'), ('#40E0D0', 'Turquoise'), ('#20B2AA', 'LightSeaGreen'),
        ('#48D1CC', 'MediumTurquoise'), ('#008B8B', 'Dark Cyan'), ('#00FFFF', 'Aqua'), ('#00CED1', 'Dark Turquoise'),
        ('#00BFFF', 'Deep Sky Blue'), ('#1E90FF', 'Dodger Blue'), ('#4169E1', 'Royal Blue'), ('#000080', 'Navy'),
        ('#00008B', 'Dark Blue'), ('#0000CD', 'Medium Blue'), ('#0000FF', 'Blue'), ('#8A2BE2', 'Blue Violet'),
        ('#9932CC', 'Dark Orchid'), ('#9400D3', 'Dark Violet'), ('#800080', 'Purple'), ('#8B008B', 'Dark Magenta'),
        ('#FF00FF', 'Magenta'), ('#C71585', 'Medium Violet Red'), ('#FF1493', 'Deep Pink'), ('#FF69B4', 'Hot Pink'),
        ('#DC143C', 'Crimson'), ('#A52A2A', 'Brown'), ('#CD5C5C', 'Indian Red'), ('#BC8F8F', 'Rosy Brown'),
        ('#F08080', 'Light Coral'), ('#FFFAFA', 'Snow'), ('#FFE4E1', 'Misty Rose'), ('#E9967A', 'Dark Salmon'),
        ('#FFA07A', 'Light Salmon'), ('#A0522D', 'Sienna'), ('#FFF5EE', 'Sea Shell'), ('#8B4513', 'Saddle Brown'),
        ('#FFDAB9', 'Peachpuff'), ('#CD853F', 'Peru'), ('#FAF0E6', 'Linen'), ('#FFE4C4', 'Bisque'),
        ('#DEB887', 'Burlywood'), ('#D2B48C', 'Tan'), ('#FAEBD7', 'Antique White'), ('#FFDEAD', 'Navajo White'),
        ('#FFEBCD', 'Blanched Almond'), ('#FFEFD5', 'Papaya Whip'), ('#FFE4B5', 'Moccasin'), ('#F5DEB3', 'Wheat'),
        ('#FDF5E6', 'Oldlace'), ('#FFFAF0', 'FloralWhite'), ('#FFF8DC', 'Cornsilk'), ('#F0E68C', 'Khaki'),
        ('#FFFACD', 'Lemon Chiffon'), ('#EEE8AA', 'Pale Goldenrod'), ('#BDB76B', 'Dark Khaki'), ('#F5F5DC', 'Beige'),
        ('#FAFAD2', 'Light Goldenrod Yellow'), ('#FFFFE0', 'Light Yellow'), ('#FFFFF0', 'Ivory'), ('#6B8E23', 'Olive Drab'),
        ('#556B2F', 'Dark Olive Green'), ('#8FBC8F', 'Dark Sea Green'), ('#006400', 'Dark Green'), ('#228B22', 'ForestGreen'),
        ('#90EE90', 'Light Green'), ('#98FB98', 'PaleGreen'), ('#F0FFF0', 'Honeydew'), ('#2E8B57', 'Sea Green'),
        ('#3CB371', 'Medium Sea Green'), ('#F5FFFA', 'Mintcream'), ('#66CDAA', 'Medium Aquamarine'), ('#7FFFD4', 'Aquamarine'),
        ('#2F4F4F', 'Dark Slate Gray'), ('#AFEEEE', 'Pale Turquoise'), ('#E0FFFF', 'Light Cyan'), ('#F0FFFF', 'Azure'),
        ('#5F9EA0', 'Cadet Blue'), ('#B0E0E6', 'Powder Blue'), ('#ADD8E6', 'Light Blue'), ('#87CEEB', 'Sky Blue'),
        ('#87CEFA', 'Lightsky Blue'), ('#4682B4', 'Steel Blue'), ('#F0F8FF', 'Alice Blue'), ('#708090', 'Slate Gray'),
        ('#778899', 'Light Slate Gray'), ('#B0C4DE', 'Lightsteel Blue'), ('#6495ED', 'Cornflower Blue'), ('#E6E6FA', 'Lavender'),
        ('#F8F8FF', 'Ghost White'), ('#191970', 'Midnight Blue'), ('#6A5ACD', 'Slate Blue'), ('#483D8B', 'Dark Slate Blue'),
        ('#7B68EE', 'Medium Slate Blue'), ('#9370DB', 'Medium Purple'), ('#4B0082', 'Indigo'), ('#BA55D3', 'Medium Orchid'),
        ('#DDA0DD', 'Plum'), ('#EE82EE', 'Violet'), ('#D8BFD8', 'Thistle'), ('#DA70D6', 'Orchid'),
        ('#FFF0F5', 'LavenderB lush'), ('#DB7093', 'Pale Violet Red'), ('#FFC0CB', 'Pink'), ('#FFB6C1', 'LightPink'),
        ('#000000', 'Black'), ('#696969', 'DimGray'), ('#808080', 'Gray'), ('#A9A9A9', 'Dark Gray'),
        ('#C0C0C0', 'Silver'), ('#D3D3D3', 'Light Grey'), ('#DCDCDC', 'Gainsboro'), ('#F5F5F5', 'White Smoke'),
        ('#FFFFFF', 'White')
    )

    # Identity details
    name = models.CharField( max_length=50 )
    aliases = models.CharField( max_length=200 )
    bio = models.TextField( null=True )
    affiliations = models.CharField( max_length=100 )

    # Physical attributes
    skin_color = models.CharField( max_length=8, choices=SKIN_COLOR_CHOICES )
    height = models.DecimalField( max_digits=4, decimal_places=2 )
    weight = models.DecimalField( max_digits=4, decimal_places=2 )