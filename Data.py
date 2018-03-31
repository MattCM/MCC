# This file holds lists of the different types of NBT tags
NBT_BYTE_TAGS = ["IsVillager","Ambient","Amplifier","Angry","AttachFace","auto","BatFlags","Bred","CanBreakDoors","CanPickUpLoot","ChestedHorse","CollarColor","Color","Count","conditionMet","crit","CustomDisplayTile","CustomNameVisible","damage","Data","DropItem","EatingHaystack","Enabled","ExactTeleport","ExplosionRadius","extending","Facing","FallFlying","Flicker","Flight","Fuel","Glowing","Health","HurtEntities","Id","ignited","ignoreEntities","inData","inGround","instabuild","Invisible","Invulnerable","invulnerable","IsBaby","IsChickenJockey","isMovable","ItemRotation","Johnny","Leashed","LeftHanded","LightPopulated","map_tracking_position","Marker","mayBuild","mayfly","NoAI","NoBasePlate","NoGravity","note","OnGround","Peek","PersistenceRequired","pickup","player","PlayerCreated","PlayerSpawned","powered","Pumpkin","rewardExp","Rot","Saddle","seenCredits","shake","Sheared","ShowArms","ShowBottom","ShowParticles","Silent","Sitting","SkeletonTrap","SkullType","Sleeping","Slot","Small","source","SpawnForced","SplashPotion","Tame","TerrainPopulated","TrackOutput","Trail","Type","type","Unbreakable", "UpdateLastExecution","V","wasOnGround","Willing","Y"]
NBT_SHORT_TAGS = ["Age","Air","Anger","BurnTime","carried","carriedData","CookTime","CookTimeTotal","Damage","DeathTime","Delay","Fire","Fuel","Fuse","Health","HurtTime","life","MaxNearbyEntities","MaxSpawnDelay","MinSpawnDelay","PickupDelay","PotionId","RequiredPlayerRange","SleepTimer","SpawnCount","SpawnRange","Value"]
NBT_INTEGER_TAGS = ["Age","APX","APY","APZ","Base","blockData","blockId","BoundX","BoundY","BoundZ","BrewTime","Career","CareerLevel","CatType","Color","color","ConversionTime","CustomColor","CustomPotionColor","Data","DataVersion","Dimension","DisabledSlots","DisplayData","DisplayOffset","DragonPhase","Duration","EggLayTime","ExplosionPower","facing","FallHurtMax","foodLevel","foodTickTimer","ForcedAge","Generation","HideFlags","HurtByTimestamp","inLove","Invul","L","Levels","Life","life","LifeTicks","LifeTime","Lifetime","M","map_scale_direction","MapColor","maxUses","MoreCarrotTicks","Operation","OutputSignal","p","ParticleParam1","ParticleParam2","playerGameType","PortalCooldown","posX","posY","posZ","Primary","Profession","RabbitType","ReapplicationDelay","Record","RepairCost","Riches","Score","Secondary","SelectedItemSlot","Size","sizeX","sizeY","sizeZ","SkeletonTrapTime","SpawnX","SpawnY","SpawnZ","SpellTicks","Steps","Strength","SuccessCount","t","Temper","TileID","TileX","TileY","TileZ","Time","TNTFuse","TransferCooldown","uses","Variant","WaitTime","Warmup","Weight","X","x","XpLevel","xPos","XpSeed","XpTotal","xTile","Y","y","yTile","Z","z","zPos","zTile"]
NBT_LONG_TAGS = ["Age","AttachLeast","AttachMost","ConversionPlayerLeast","ConversionPlayerMost","DeathLootTableSeed","InhabitedTime","L","LastExecution","LastUpdate","LootTableSeed","LoveCauseLeast","LoveCauseMost","M","OwnerUUIDLeast","OwnerUUIDMost","UUIDLeast","UUIDMost","XYZ"]
NBT_FLOAT_TAGS = ["0","1","2","3","4","AbsorptionAmount","DurationOnUse","FallDistance","FallHurtAmount","flySpeed","foodExhaustionLevel","foodSaturationLevel","Health","ItemDropChance","progress","Radius","RadiusOnUse","RadiusPerTick","walkSpeed","XpP"]
NBT_DOUBLE_TAGS = ["Amount","Base","damage","PushX","PushZ","rot","TXD","TYD","TZD","x","y","z"]
NBT_STRING_TAGS = ["AffectedBlocksName","AffectedBlocksObjective","AffectedEntitiesName","AffectedEntitiesObjective","AffectedItemsName","AffectedItemsObjective","author","Block","carried","Command","CustomName","DeathLootTable","DisplayTile","HurtBy","i","id","Id","inTile","Item","LastOutput","Lock","LocName","LootTable","metadata","mirror","mode","Motive","Name","name","Owner","ownerName","OwnerUUID","Particle","Pattern","Potion","QueryResultName","QueryResultObjective","rotation","Signature","SuccessCountName","SuccessCountObjective","Team","Text1","Text2","Text3","Text4","Thrower","Type","Value"]
NBT_COMPOUND_TAGS = ["recipeBook","Leash","pages","abilities","Entity","RootVehicle","Passengers","Tags","CommandStats","SelectedItem","EnderItems","DecorItem","Item","ArmorItem","SaddleItem","Offers","Recipes","buy","buyB","sell","tag","Potion","SpawnPotentials","Properties","SpawnData","TileEntityData","Effects","0","1","2","3","4","Pose","BeamTarget","FireworksItem","Explosion","Explosions","Fireworks","Colors","FadeColors","Owner","Target","Patterns","ExitPortal","RecordItem","Textures","CanDestroy","CanPlaceOn","ench","BlockEntityTag","display","SkullOwner","textures","Value","SKIN","CAPE","EntityTag","Decorations","ShoulderEntityLeft","ShoulderEntityRight"]
NBT_STRING_LIST_TAGS = ["Lore", "Tags"]
NBT_INTEGER_LIST_TAGS = ["Colors", "FadeColors"]
NBT_FLOAT_LIST_TAGS = ["Pos","Motion","direction","power","Body","LeftArm","RightArm","LeftLeg","RightLeg","Head","Rotation"]
NBT_COMPOUNT_LIST_TAGS = ["Attributes", "ActiveEffects", "HandItems","ArmorItems","Inventory","Items","CustomPotionEffects","AttributeModifiers","StoredEnchantments","textures","Passengers"]
PARTICLES = ["ambient_entity_effect","angry_villager","block","damage_indicator","dragon_breath","dripping_lava","dripping_water","dust","effect","elder_guardian","enchant","enchanted_hit","end_rod","entity_effect","explosion","explosion_emitter","falling_dust","firework","fishing","happy_villager","instant_effect","item","item_slime","item_snowball","large_smoke","mycelium","poof","rain","sweep_attack","totem_of_undying","underwater","witch", "smoke"]
JSON_STRING_KEYS = ["text","insertion","title","author","translate","command","keybind"]
JSON_ENTITY_KEYS = ["selector","markerTag"]
JSON_BOOLEAN_KEYS = ["bold","italic","underlined","strikethrough","obfuscated"]
JSON_NESTED_KEYS = ["with", "extra"]