from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render (request, 'home.html')

def about(request):
  return render(request, 'about.html')

def hero_detail(request, hero):
  return render(request, 'heroes/detail.html', {'hero': hero})

class Hero:
  def __init__(self, name, role, rating, description, weapon, abilities, background, portrait):
    self.name = name
    self.role = role
    self.rating = rating
    self.description = description
    self.weapon = weapon
    self.abilities = abilities
    self.background = background
    self.portrait = portrait

heroes = [
  Hero('Ana', 'Support', 3, "Ana’s versatile arsenal allows her to affect heroes all over the battlefield. Her Biotic Rifle rounds and Biotic Grenades heal allies and damage or impair enemies; her sidearm tranquilizes key targets, and Nano Boost gives one of her comrades a considerable increase in power.", 'Biotic Rifle', 'Sleep Dart, Biotic Grenade, Nano Boost', 'https://d1u1mce87gyfbn.cloudfront.net/hero/ana/idle-video.webm', 'https://d1u1mce87gyfbn.cloudfront.net/hero/ana/hero-select-portrait.png'),
  Hero('Ashe', 'Damage', 2, "Ashe quickly fires her rifle from the hip or uses her weapon’s aim-down sights to line up a high damage shot. She blasts enemies by throwing dynamite, and her coach gun packs enough punch to put some distance between her and her foes. And Ashe is not alone, as she can call on her omnic ally Bob, to join the fray when the need arises.", "The Viper - Rifle", "Coach Gun, Dynamite, B.O.B.","https://d1u1mce87gyfbn.cloudfront.net/hero/ashe/idle-video.webm", "https://d1u1mce87gyfbn.cloudfront.net/hero/ashe/hero-select-portrait.png"),
  Hero('Baptiste', "Support", 3, "Baptiste wields an assortment of experimental devices and weaponry to keep allies alive and eliminate threats under fierce conditions. A battle-hardened combat medic, he is just as capable of saving lives as he is taking out the enemy.", 'Biotic Launcher', 'Regenerative Burst, Immortality Field, Exo Boots, Amplification Matrix', 'https://d1u1mce87gyfbn.cloudfront.net/hero/baptiste/idle-video.webm', 'https://d1u1mce87gyfbn.cloudfront.net/hero/baptiste/hero-select-portrait.png'),
  Hero('Bastion', 'Damage', 1, "Repair protocols and the ability to transform between stationary Assault, mobile Recon and devastating Tank configurations provide Bastion with a high probability of victory.", 'Configuration: Sentry, Configuration: Recon', 'Self-Repair, Reconfigure, Ironclad, Configuration: Tank', 'https://d1u1mce87gyfbn.cloudfront.net/hero/bastion/idle-video.webm', 'https://d1u1mce87gyfbn.cloudfront.net/hero/bastion/hero-select-portrait.png'),
  Hero('Brigitte', 'Support', 1, "Brigitte specializes in armor. She can throw Repair Packs to heal teammates, or automatically heal nearby allies when she damages foes with her Flail. Her Flail is capable of a wide swing to strike multiple targets, or a Whip Shot that stuns an enemy at range. When entering the fray, Barrier Shield provides personal defense while she attacks enemies with Shield Bash. Brigitte’s ultimate ability, Rally, gives her a substantial short-term boost of speed and provides long-lasting armor to all her nearby allies.", 'Rocket Flail', 'Repair Pack, Whip Shot, Barrier Shield, Shield Bash, Inspire, Rally', 'https://d1u1mce87gyfbn.cloudfront.net/hero/brigitte/idle-video.webm', 'https://d1u1mce87gyfbn.cloudfront.net/hero/brigitte/hero-select-portrait.png'),
  Hero('Cassidy', 'Damage', 2, "Armed with his Peacekeeper revolver, Cassidy takes out targets with deadeye precision and dives out of danger with eagle-like speed.", 'Peacekeeper', 'Combat Roll, Flashbang, Deadeye', 'https://d1u1mce87gyfbn.cloudfront.net/hero/cassidy/idle-video.webm', 'https://d1u1mce87gyfbn.cloudfront.net/hero/cassidy/hero-select-portrait.png'),
  Hero('DVa', 'Tank', 2, "D.Va’s mech is nimble and powerful—its twin Fusion Cannons blast away with autofire at short range, and she can use its Boosters to barrel over enemies and obstacles, or deflect attacks with her projectile-dismantling Defense Matrix.", 'Fusion Cannons, Light Gun', 'Boosters, Defense Matrix, Micro Missiles, Call Mech, Eject, Self-Destruct', 'https://d1u1mce87gyfbn.cloudfront.net/hero/dva/idle-video.webm', 'https://d1u1mce87gyfbn.cloudfront.net/hero/dva/hero-select-portrait.png'),
  Hero('Doomfist', 'Damage', 3, "Doomfist’s cybernetics make him a highly-mobile, powerful frontline fighter. In addition to dealing ranged damage with his Hand Cannon, Doomfist can slam the ground, knock enemies into the air and off balance, or charge into the fray with his Rocket Punch. When facing a tightly packed group, Doomfist leaps out of view, then crashes down to earth with a spectacular Meteor Strike.", 'Hand Cannon', 'Seismic Slam, Rising Uppercut, Rocket Punch, Meteor Strike', 'https://d1u1mce87gyfbn.cloudfront.net/hero/doomfist/idle-video.webm', 'https://d1u1mce87gyfbn.cloudfront.net/hero/doomfist/hero-select-portrait.png'),
]

def hero_list(request):
  return render(request, 'heroes/list.html', {'heroes': heroes})